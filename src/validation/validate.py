
import json

from datetime import datetime
from pathlib import Path

import pandas as pd

from src.config.settings import PROJECT_ROOT
from src.ingestion.extract import extract_dataset

from src.validation.schema import validate_schema
from src.validation.data_quality import validate_data_quality


# ============================================================
# CONFIGURACION
# ============================================================

VALIDATION_REPORT_DIR = (
    PROJECT_ROOT
    / "src"
    / "validation"
    / "reports"
)


# ============================================================
# VALIDACIÓN DE ORQUESTACIÓN
# ============================================================

def validate_dataset(df: pd.DataFrame) -> dict:
    """
    Ejecuta el proceso completo de validación del dataset.

    Primero, se realiza la validación del esquema.
    La validación de la calidad de los datos solo es ejecutada
    el esquema no presenta fallos críticos.
    """

    resultados_esquema = validate_schema(df)

    falla_esquema = any(
        result["Estado"] == "FAIL"
        for result in resultados_esquema
    )

    if falla_esquema:

        resultados_calidad = [{
            "Verificar": "Data quality execution",
            "Estado": "WARN",
            "Detalles": (
                "Se omitieron las comprobaciones de la calidad de los datos porque"
                "la validación del esquema."
            ),
            "affected_rows": 0,
            "affected_columns": 0
        }]

    else:

        resultados_calidad = validate_data_quality(df)

    all_results = resultados_esquema + resultados_calidad

    has_failures = any(
        result["Estado"] == "FAIL"
        for result in all_results
    )

    has_warnings = any(
        result["Estado"] == "WARN"
        for result in all_results
    )

    if has_failures:
        overall_Estado = "FAIL"

    elif has_warnings:
        overall_Estado = "WARN"

    else:
        overall_Estado = "PASS"

    return {
        "Estado": overall_Estado,
        "dataset": {
            "filas": len(df),
            "columnas": len(df.columns)
        },
        "resumen": {
            "verificacion_total": len(all_results),
            "passed": sum(
                r["Estado"] == "PASS" for r in all_results
            ),
            "warnings": sum(
                r["Estado"] == "WARN" for r in all_results
            ),
            "failed": sum(
                r["Estado"] == "FAIL" for r in all_results
            )
        },
        "resultados": all_results
    }


# ============================================================
# GENERACION DE REPORTE
# ============================================================

def save_validation_report(report: dict) -> None:
    """
    Guarda los resultados de la validacion en formato CSV y JSON.
    """

    VALIDATION_REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")            # funcion para obtener fecha + hora + tiempo actual

    report_df = pd.DataFrame(report["resultados"])

    csv_path = (
        VALIDATION_REPORT_DIR
        / f"validation_report_{timestamp}.csv"
    )

    json_path = (
        VALIDATION_REPORT_DIR
        / f"validation_report_{timestamp}.json"
    )

    report_df.to_csv(
        csv_path,
        index=False,
        encoding="utf-8-sig"
    )

    json_report = {
        **report,
        "generated_at": datetime.now().astimezone().isoformat()
    }

    with open(json_path, "w", encoding="utf-8") as file:

        json.dump(
            json_report,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\n--- VALIDATION REPORT ---")
    print(f"Overall Estado: {report['Estado']}")
    print(f"Total checks: {report['resumen']['verificacion_total']}")
    print(f"Passed: {report['resumen']['passed']}")
    print(f"Warnings: {report['resumen']['warnings']}")
    print(f"Failed: {report['resumen']['failed']}")

    print(f"\nCSV report: {csv_path}")
    print(f"JSON report: {json_path}")


# ============================================================
# EJECUCION PRNCIPAL
# ============================================================

def run_validation() -> dict:
    """
    Extrae el dataset, ejecuta las validaciones,
    genera reportes y devuelve los resultados.
    """

    df = extract_dataset()

    report = validate_dataset(df)

    save_validation_report(report)

    return report


if __name__ == "__main__":

    run_validation()
