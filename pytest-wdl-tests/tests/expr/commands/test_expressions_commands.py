def test_expressions_commands(workflow_runner):
    """
    Expression evaluation in commands.
    """
    inputs = { }
    """
    Expectations are possibly not 100% as Cromwell 48 doesn't come close to being able to deal 
    with this workflow.
    """
    expected = {
        "exprs.string": "string",
        "exprs.parens": "string",
        "exprs.left": "left",
        "exprs.var_left": "left",
        "exprs.array_element": "string",
        "exprs.true_": "true",
        "exprs.false_": "false",
        "exprs.negated": "false",
        "exprs.true_var": "true",
        "exprs.false_var": "false",
        "exprs.negated_var": "false",
        "exprs.forty_two": "42",
        "exprs.plus_forty_two": "42",
        "exprs.minus_forty_two": "-42",
        "exprs.i": "42",
        "exprs.plus_i": "42",
        "exprs.minus_i": "-42",
        "exprs.conditional": "1",
        "exprs.conditional_var": "1",
        "exprs.mult": "1806",
        "exprs.mult_var": "1806",
        "exprs.div": "0",
        "exprs.div_var": "0",
        "exprs.mod": "42",
        "exprs.mod_var": "42",
        "exprs.add": "85",
        "exprs.add_var": "85",
        "exprs.sub": "-1",
        "exprs.sub_var": "-1",
        "exprs.lt": "true",
        "exprs.lt_var": "true",
        "exprs.lte": "true",
        "exprs.lte_var": "true",
        "exprs.gt": "false",
        "exprs.gt_var": "false",
        "exprs.gte": "false",
        "exprs.gte_var": "false",
        "exprs.eq": "false",
        "exprs.eq_var": "false",
        "exprs.ne": "true",
        "exprs.ne_var": "true",
        "exprs.and": "false",
        "exprs.and_var": "false",
        "exprs.or": "true",
        "exprs.or_var": "true",
        "exprs.jamie": "Jamie",
        "exprs.jamie_var": "Jamie",
        "exprs.array_literal": "string",
        "exprs.array_": True,
        "exprs.array__": True
    }
    workflow_runner(
        "test_expressions_commands.wdl",
        inputs,
        expected,
        workflow_name = "commands"
    )
