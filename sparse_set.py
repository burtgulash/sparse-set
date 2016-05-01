class SparseSet:

    def __init__(self, size, maxvalue):
        self._dense = [0 for x in range(size)]
        self._sparse = [0 for x in range(maxvalue)]
        self._m = maxvalue
        self._n = 0

    def clear(self):
        self._n = 0

    def __contains__(self, x):
        return self._sparse[x] < self._n and \
               self._dense[self._sparse[x]] == x

    def __len__(self):
        return self._n

    def __iter__(self):
        return self._Iter(self)

    def add(self, x):
        if x <= 0 or self._m <= x:
            raise ValueError("Value inserted outside of set range: 0 - %s" % str(self._m - 1))
        if self._n >= len(self._dense):
            raise self.SetFullError("Set is full!")
        if x in self:
            return
        self._dense[self._n] = x
        self._sparse[x] = self._n
        self._n += 1

    class SetFullError(Exception):
        pass

    class _Iter:

        def __init__(self, sset):
            self._i = 0
            self._sset = sset

        def __next__(self):
            if self._i >= len(self._sset):
                raise StopIteration
            self._i += 1
            return self._sset._dense[self._i - 1]


