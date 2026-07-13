class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        minT = float('inf')
        minI = -1
        for ind,i in enumerate(self.d[key]):
            if i[0]<=timestamp:
                # print(i)
                minT = i[0]
                minI = ind
        print(minI,self.d[key])
        return self.d[key][minI][1] if minI!=-1 else ""
