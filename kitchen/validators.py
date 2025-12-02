from django import forms


def validate_years_of_experience(value: int) -> None:
    if value < 0 or value > 100:
        raise forms.ValidationError("Years of experience must be between 0 and 100.")
