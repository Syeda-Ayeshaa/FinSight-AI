def validate_totals(data, table_df):

    subtotal = table_df["line_total"].sum()

    tax = data.get("tax", 0)
    actual_total = data.get("total", 0)

    expected_total = subtotal + tax

    # Build step-by-step explanation
    steps = []
    values = []

    for _, row in table_df.iterrows():
        step = f"{row['qty']} × {row['price']} = {row['line_total']}"
        steps.append(step)
        values.append(str(row["line_total"]))

    subtotal_step = " + ".join(values)

    explanation_steps = steps
    subtotal_explanation = f"Subtotal = {subtotal_step} = {subtotal}"

    final_explanation = f"Final Total = {subtotal} + {tax} = {expected_total}"

    if abs(expected_total - actual_total) < 1:
        status = "VALID"
        explanation = "Invoice totals match calculated values."
    else:
        status = "ERROR"
        explanation = "Invoice total does not match subtotal + tax."

    result = {
        "computed_subtotal": float(subtotal),
        "tax": float(tax),
        "expected_total": float(expected_total),
        "actual_total": float(actual_total),
        "status": status,
        "explanation": explanation,
        "calculation_steps": explanation_steps,
        "subtotal_explanation": subtotal_explanation,
        "final_explanation": final_explanation
    }

    return result