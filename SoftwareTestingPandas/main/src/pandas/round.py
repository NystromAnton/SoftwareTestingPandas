def round(self, decimals=0, *args, **kwargs) -> "DataFrame": 
    
8043        from pandas.core.reshape.concat import concat 
8044 
8045        def _dict_round(df, decimals): 
8046            for col, vals in df.items(): 
8047                try: 
8048                    yield _series_round(vals, decimals[col]) 
8049                except KeyError: 
8050                    yield vals 
8051 
8052        def _series_round(s, decimals): 
8053            if is_integer_dtype(s) or is_float_dtype(s): 
8054                return s.round(decimals) 
8055            return s 
8056 
8057        nv.validate_round(args, kwargs) 
8058 
8059        if isinstance(decimals, (dict, Series)): 
8060            if isinstance(decimals, Series): 
8061                if not decimals.index.is_unique: 
8062                    raise ValueError("Index of decimals must be unique") 
8063            new_cols = list(_dict_round(self, decimals)) 
8064        elif is_integer(decimals): 
8065            # Dispatch to Series.round 
8066            new_cols = [_series_round(v, decimals) for _, v in self.items()] 
8067        else: 
8068            raise TypeError("decimals must be an integer, a dict-like or a Series") 
8069 
8070        if len(new_cols) > 0: 
8071            return self._constructor( 
8072                concat(new_cols, axis=1), index=self.index, columns=self.columns 
8073            ) 
8074        else: 
8075            return self 