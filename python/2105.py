class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        i, j = 0, len(plants) - 1
        curA, curB = capacityA, capacityB
        res = 0
        while (i < j):
            if curA >= plants[i]:
                curA -= plants[i]
            else:
                curA = capacityA - plants[i]
                res += 1
            i += 1
            if curB >= plants[j]:
                curB -= plants[j]
            else:
                curB = capacityB - plants[j]
                res += 1
            j -= 1

        if i == j:
            if max(curA, curB) < plants[i]:
                res += 1
                
        return res