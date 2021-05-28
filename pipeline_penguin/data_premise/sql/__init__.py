"""Main data_premise package, contains high-level data_nodes for SQL-based data premises (BigQuery,
MySQL, etc).

This package provides `DataPremise` constructors, which are pre-written validations to be executed
against a `DataNode`. This package only convers SQL-based validations.

Location: pipeline_penguin/data_premise/sql
"""
# TODO: Rebuild/rename the modules for a more inuitive approach.
# check_distinct -> Is OK if all values are distinct
# check_null -> IS OK if all values are NOT null
# check_between -> Is OK if the values belong to a given set
# checks_regex -> Is OK if the values matches a pattern
from .check_null import DataPremiseSQLCheckIsNull
from .check_distinct import DataPremiseSQLCheckDistinct
from .check_arithmetic import DataPremiseSQLCheckArithmeticOperationEqualsResult
from .check_between import DataPremiseSQLCheckValuesAreBetween
from .check_in import DataPremiseSQLCheckInArray
from .check_like import DataPremiseSQLCheckLikePattern
from .check_regexp import DataPremiseSQLCheckRegexpContains
from .check_comparison import DataPremiseSQLCheckLogicalComparisonWithValue

__all__ = [
    "DataPremiseSQLCheckIsNull",
    "DataPremiseSQLCheckDistinct",
    "DataPremiseSQLCheckArithmeticOperationEqualsResult",
    "DataPremiseSQLCheckValuesAreBetween",
    "DataPremiseSQLCheckInArray",
    "DataPremiseSQLCheckLikePattern",
    "DataPremiseSQLCheckRegexpContains",
    "DataPremiseSQLCheckLogicalComparisonWithValue",
]
