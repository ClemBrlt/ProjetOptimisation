class FonctionsProduction:

    def productionturbinei(self, debit, hchute, turbine):
        if turbine == 0:
            return self.turbine1(debit, hchute)
        if turbine == 1:
            return self.turbine2(debit, hchute)
        if turbine == 2:
            return self.turbine3(debit, hchute)
        if turbine == 3:
            return self.turbine4(debit, hchute)
        if turbine == 4:
            return self.turbine5(debit, hchute)

    def turbine1(self, debit, hchute):
        pmw = 3.468 * pow(10, -5) * pow(debit, 3) - 0.02772 * pow(debit, 2) + 3.121 * debit + 0.264 * pow(hchute, 2) \
              - 13.41 * hchute + 3.116 * pow(10, -4) * pow(debit, 2) * hchute - 0.001919 * debit * pow(hchute, 2) \
              + 0.06052 * debit * hchute + 14.66
        return pmw

    def turbine2(self, debit, hchute):
        pmw = 1.664 * pow(10, -6) * pow(debit, 4) - 0.0011 * pow(debit, 3) + 0.599 * pow(debit,2) - 131.8 * debit \
              + 6.876 * pow(hchute, 2) - 481.1 * hchute + 4.083 * pow(10, -6) * pow(debit, 3) * hchute \
              + 2.888 * pow(10, -6) * pow(debit, 2) * pow(hchute, 2) - 0.02145 * pow(debit, 2) * hchute \
              - 0.08983 * debit * pow(hchute, 2) + 6.387 * debit * hchute + 9044
        return pmw

    def turbine3(self, debit, hchute):
        pmw = 6.162 * pow(10, -5) * pow(debit, 3) - 0.03789 * pow(debit, 2) + 2.852 * debit \
              + 0.5212 * pow(hchute, 2) - 28.94 * hchute + 2.034 * pow(10, -4) * pow(debit, 2) * hchute \
              - 0.004112 * debit * pow(hchute, 2) + 0.2127 * debit * hchute + 115.4
        return pmw

    def turbine4(self, debit, hchute):
        pmw = 1.442 * pow(10, -6) * pow(debit, 4) - 7.896 * pow(10, -4) * pow(debit, 3) + 0.07851 * pow(debit, 2) \
              + 9.675 * debit - 1.577 * pow(hchute, 2) + 109 * hchute - 1.248 * pow(10, -6) * pow(debit, 3) * hchute \
              - 7.439 * pow(10, -5) * pow(debit, 2) * pow(hchute, 2) + 0.005468 * pow(debit, 2) * hchute \
              + 0.02124 * debit * pow(hchute, 2) - 1.481 * debit * hchute - 1331
        return pmw

    def turbine5(self, debit, hchute):
        pmw = 1.615 * pow(10, -5) * pow(debit, 3) + 0.001932 * pow(debit, 2) - 1.935 * debit - 0.06146 * pow(hchute, 2) \
              - 3.99 * hchute - 3.386 * pow(10, -4) * pow(debit, 2) * hchute \
              - 4.68 * pow(10, -5) * debit * pow(hchute, 2) + 0.118 * debit * hchute + 111.1
        return pmw
