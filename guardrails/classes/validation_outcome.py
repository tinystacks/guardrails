from typing import Dict, Union

from pydantic import Field

from guardrails.utils.logs_utils import ArbitraryModel, GuardHistory


class ValidationOutcome(ArbitraryModel):
    raw_llm_output: str = Field(
        description="The raw, unchanged output from the LLM call."
    )
    validated_output: Union[str, Dict, None] = Field(
        description="The validated, and potentially fixed,"
        " output from the LLM call after passing through validation."
    )
    validation_passed: bool = Field(
        description="A boolean to indicate whether or not"
        " the LLM output passed validation."
        "  If this is False, the validated_output may be invalid."
    )

    @classmethod
    def from_guard_history(cls, guard_history: GuardHistory):
        raw_output = guard_history.output
        validated_output = guard_history.validated_output
        any_validations_failed = len(guard_history.failed_validations) > 0
        if isinstance(validated_output, str):
            return TextOutcome(
                raw_llm_output=raw_output,
                validated_output=validated_output,
                validation_passed=any_validations_failed,
            )
        else:
            return StructuredOutcome(
                raw_llm_output=raw_output,
                validated_output=validated_output,
                validation_passed=any_validations_failed,
            )


class TextOutcome(ValidationOutcome):
    validated_output: Union[str, None] = Field(
        description="The validated, and potentially fixed,"
        " output from the LLM call after passing through validation."
    )


class StructuredOutcome(ValidationOutcome):
    validated_output: Union[Dict, None] = Field(
        description="The validated, and potentially fixed,"
        " output from the LLM call after passing through validation."
    )
