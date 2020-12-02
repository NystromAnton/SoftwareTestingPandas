def _make_stat_function(
    cls,
    name: str,
    name1: str,
    name2: str,
    axis_descr: str,
    desc: str,
    func: Callable,
    see_also: str = "",
    examples: str = "",
) -> Callable:
    @Substitution(
        desc=desc,
        name1=name1,
        name2=name2,
        axis_descr=axis_descr,
        min_count="",
        see_also=see_also,
        examples=examples,
    )
    @Appender(_num_doc)
    def stat_func(
        self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs
    ):
        if name == "median":
            nv.validate_median(tuple(), kwargs)
        else:
            nv.validate_stat_func(tuple(), kwargs, fname=name)
        if skipna is None:
            skipna = True
        if axis is None:
            axis = self._stat_axis_number
        if level is not None:
            return self._agg_by_level(name, axis=axis, level=level, skipna=skipna)
        return self._reduce(
            func, name=name, axis=axis, skipna=skipna, numeric_only=numeric_only
        )

    return set_function_name(stat_func, name, cls)