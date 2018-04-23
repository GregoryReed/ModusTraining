import timeit


def get_candies(candies: list) -> int:
    """
    Get the amount of unique candies someone would receive if
        the list of candies are split between 2 people
    :param candies: a list of candies to be shared
    :return: the max amount of unique candies someone would recive
    """
    return min(len(set(candies)), int(len(candies)/2))

def test():
    test0 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    answer = get_candies(test0)
    assert answer == 1, 'you dun goofed'

    test1 = [493, 1938, 357, 111, 1571, 912, 753, 87, 1826, 1470, 1096, 972, 179, 71,
     844, 316, 42, 684, 1041, 601, 61, 1027, 494, 483, 1399, 1665, 95, 449,
     1240, 358, 416, 123, 84, 1065, 1019, 1845, 645, 1070, 972, 819, 1982, 436,
     964, 1384, 1690, 1289, 909, 863, 1553, 889, 1827, 1798, 1610, 2, 1205,
     550, 1396, 220, 1827, 1915, 1227, 299, 518, 276, 705, 1019, 801, 1279,
     1367, 740, 1371, 1974, 750, 1868, 259, 202, 1375, 631, 274, 930, 1115,
     1278, 1360, 263, 314, 1565, 595, 575, 533, 1948, 729, 1645, 1929, 906,
     1681, 1152, 935, 647, 87, 31, 850, 910, 765, 1283, 307, 1513, 1316, 1837,
     1915, 922, 1331, 1825, 1428, 220, 1974, 1990, 129, 1820, 1614, 1691, 829,
     731, 546, 739, 530, 422, 1631, 308, 1821, 1466, 1773, 344, 27, 803, 1967,
     1754, 1921, 326, 484, 870, 1451, 131, 570, 1876, 1019, 1570, 348, 850,
     1771, 465, 1987, 283, 755, 1923, 1561, 70, 651, 1321, 503, 315, 1863,
     1825, 1368, 1886, 470, 795, 849, 1406, 1750, 538, 819, 175, 1526, 323,
     1241, 1826, 1879, 672, 1583, 952, 1708, 898, 1246, 904, 1239, 1136, 1946,
     1268, 1029, 935, 1926, 323, 57, 1049, 974, 845, 1340, 526, 1690, 1919,
     779, 804, 5, 1674, 974, 536, 450, 732, 846, 932, 1379, 1644, 1047, 313,
     1405, 1133, 8, 2008, 738, 1411, 1684, 1521, 244, 1723, 79, 1612, 1172,
     1940, 186, 74, 719, 1006, 1427, 255, 1568, 222, 602, 1152, 36, 735, 559,
     678, 539, 1737, 719, 875, 1096, 507, 55, 1668, 420, 1235, 1702, 950, 767,
     1066, 924, 1527, 448, 931, 618, 91, 229, 826, 835, 1280, 105, 568, 163,
     1486, 1478, 743, 131, 784, 486, 477, 1506, 1155, 1638, 1746, 1961, 840,
     1435, 2014, 1716, 1720, 1426, 1864, 1354, 1407, 1287, 1323, 1612, 450,
     1132, 325, 114, 1224, 298, 674, 1367, 1087, 678, 772, 138, 1504, 583, 132,
     1680, 921, 1809, 1020, 165, 1824, 433, 972, 1428, 1139, 1730, 703, 932,
     555, 846, 1375, 1531, 2017, 1774, 774, 737, 175, 138, 1902, 388, 156, 565,
     387, 1286, 251, 624, 1168, 1940, 879, 343, 1058, 944, 666, 1644, 1811,
     1399, 709, 37, 595, 1484, 1272, 255, 1128, 1909, 1308, 768, 1459, 1584,
     1953, 1746, 1149, 2004, 1680, 1347, 400, 1326, 362, 1105, 1228, 1649,
     1282, 55, 280, 1418, 1938, 298, 1377, 456, 408, 40, 2014, 1830, 1838, 291,
     2011, 542, 1260, 755, 1292, 1989, 436, 1933, 1344, 1730, 925, 42, 172,
     1652, 1285, 1870, 610, 86, 1271, 780, 800, 1024, 1676, 1012, 53, 926, 33,
     1516, 1605, 542, 690, 1456, 754, 2013, 1873, 1928, 79, 1808, 365, 816,
     1539, 585, 1014, 1661, 1501, 545, 1396, 1395, 731, 1636, 616, 1990, 1726,
     1941, 526, 1377, 723, 1862, 133, 561, 507, 96, 1876, 1753, 1919, 1783,
     1121, 7, 1539, 1275, 1919, 246, 779, 414, 784, 1426, 1351, 1631, 1858,
     1213, 92, 702, 93, 1812, 1519, 901, 1467, 230, 75, 68, 1766, 1342, 1147,
     338, 106, 184, 855, 315, 1816, 1922, 1986, 980, 66, 1536, 1256, 1996, 687,
     2015, 1104, 205, 603, 1230, 1201, 1649, 158, 601, 591, 1209, 1471, 181,
     906, 1272, 1109, 159, 1366, 1163, 241, 1645, 1400, 1929, 1973, 1787, 1532,
     1149, 1047, 1611, 77, 1028, 557, 1048, 873, 1830, 408, 1497, 1971, 614,
     493, 1797, 321, 467, 888, 700, 363, 49, 743, 3, 1363, 1993, 1026, 650,
     1691, 1205, 1900, 81, 340, 1739, 1931, 1569, 630, 704, 874, 1408, 1671,
     1799, 193, 1091, 1899, 1324, 1271, 1026, 653, 1704, 1758, 1207, 924, 214,
     582, 1982, 1330, 1547, 442, 370, 1280, 1150, 488, 1224, 1437, 1563, 1580,
     1493, 522, 379, 356, 1558, 889, 1811, 1684, 981, 943, 413, 602, 2004, 503,
     1653, 596, 1940, 1927, 1722, 1101, 166, 2006, 87, 1970, 49, 1645, 1081,
     191, 1612, 197, 755, 1358, 557, 7, 718, 785, 250, 631, 913, 1423, 1672,
     1259, 902, 485, 1104, 953, 103, 1078, 241, 1728, 1682, 1839, 1488, 957,
     320, 876, 1116, 1010, 1651, 1225, 1538, 467, 2, 1044, 71, 1896, 830, 552,
     1264, 1644, 517, 16, 84, 733, 78, 1331, 1867, 545, 1692, 719, 1305, 1454,
     965, 245, 1091, 536, 71, 1937, 635, 1625, 1715, 1229, 787, 190, 1404,
     1053, 417, 18, 1487, 358, 1764, 351, 837, 469, 893, 1670, 1612, 122, 1782,
     1352, 1068, 1063, 1811, 338, 632, 1406, 994, 1478, 484, 1258, 151, 647,
     737, 1036, 1014, 1128, 53, 1784, 117, 74, 722, 607, 445, 1736, 1569, 1372,
     104, 329, 209, 329, 1221, 476, 1619, 1356, 1957, 1917, 250, 20, 1040,
     1837, 925, 1921, 556, 1012, 1772, 1632, 1257, 714, 511, 1975, 1310, 896,
     1994, 435, 436, 871, 1491, 1331, 126, 302, 581, 380, 2019, 425, 69, 155,
     1376, 1877, 683, 1782, 1542, 1836, 873, 1398, 1959, 873, 92, 1475, 751,
     1470, 1103, 828, 396, 78, 84, 1476, 330, 352, 1475, 372, 2017, 1229, 1085,
     1536, 1598, 1055, 1529, 1480, 1031, 804, 1537, 25, 1858, 598, 878, 1201,
     430, 84, 880, 799, 1250, 1535, 813, 1655, 877, 1580, 847, 121, 1233, 148,
     264, 182, 661, 1550, 1892, 1784, 1633, 1915, 339, 726, 1597, 138, 22,
     1149, 322, 293, 794, 1024, 188, 539, 1966, 1946, 809, 45, 1542, 25, 533,
     1687, 1752, 637, 842, 1202, 897, 1760, 1347, 152, 293, 1448, 1692, 363,
     593, 1532, 876, 505, 1695, 1106, 1756, 1001, 1825, 1254, 2019, 317, 948,
     820, 191, 463, 920, 965, 187, 1744, 2020, 1471, 1991, 2006, 1074, 760,
     1044, 1517, 784, 1662, 816, 1363, 191, 316, 1174, 1926, 1069, 262, 691,
     368, 1948, 1259, 704, 1551, 1248, 1328, 880, 1569, 598, 974, 1397, 278,
     1426, 295, 717, 1169, 2015, 1526, 607, 217, 1758, 783, 954, 796, 511,
     1317, 1377, 366, 602, 570, 1342, 589, 1314, 1048, 1875, 1254, 1762, 672,
     1774, 477, 1195, 1125, 939, 1545, 1813, 205, 1975, 806, 697, 1283, 344,
     903, 1883, 766, 625, 1155, 280, 804, 279, 1426, 161, 393, 910, 334, 65,
     959, 708, 1421, 853, 418, 546, 1491, 194, 725, 1288, 906, 1290, 107, 182,
     604, 1515, 599, 566, 1583, 1964, 374, 2011, 311, 1133, 487, 980, 616, 726,
     201, 529, 894, 754, 74, 505, 1449, 1688, 324, 1051, 1154, 404, 586, 976,
     826, 914, 1593, 1532, 846, 487, 466, 764, 1668, 148, 1566, 1915, 794,
     1027, 315, 295, 127, 436, 1763, 1239, 985, 1344, 365, 1538, 1372, 431,
     806, 683, 385, 364, 143, 1805, 1997, 795, 538, 1778, 1541, 402, 1583,
     1617, 906, 1041, 1073, 501, 1431, 1001, 1887, 1510, 1831, 1219, 37, 1699,
     1765, 695, 1061, 564, 858, 1814, 623, 1525, 1502, 1465, 1135, 535, 585,
     549, 39, 1750, 505, 1807, 118, 1218, 738, 14, 1977, 86, 1595, 616, 483,
     127, 973, 2024, 1334, 951, 1612, 139, 387, 1012, 1416, 401, 1221, 1753,
     266, 1274, 453, 1690, 1437, 1132, 1519, 997, 1406, 1787, 968, 657, 1462,
     1717, 1044, 1815, 650, 1050, 1873, 145, 1445, 258, 1500, 708, 724, 1906,
     769, 260, 1966, 1631, 1851, 1829, 409, 1944, 372, 1688, 1429, 1193, 719,
     1828, 544, 36, 730, 1990, 2016, 397, 794, 335, 1029, 1613, 2022, 992,
     1822, 1937, 1014, 31, 214, 1027, 1892, 13, 1628, 1181, 15, 1786, 727, 866,
     1701, 2022, 1894, 1010, 713, 162, 1355, 1343, 1094, 1956, 1708, 1849,
     1045, 1375, 755, 1599, 1347, 1066, 421, 1546, 1540, 1466, 1391, 29, 1417,
     229, 1262, 989, 417, 567, 219, 1047, 1437, 984, 427, 1217, 371, 1385, 981,
     1443, 651, 1265, 1735, 1945, 786, 704, 1488, 584, 1135, 440, 1498, 1529,
     1811, 1738, 40, 1696, 544, 409, 1199, 500, 122, 220, 1394, 1380, 827,
     1348, 938, 858, 56, 254, 1331, 157, 430, 1397, 1499, 1477, 610, 409, 122,
     574, 1747, 855, 346, 213, 1626, 289, 276, 33, 846, 141, 1066, 574, 1521,
     1819, 949, 751, 1059, 1933, 772, 1610, 830, 1886, 1011, 1313, 1361, 363,
     1377, 1406, 109, 942, 1521, 1702, 1342, 1524, 2025, 531, 565, 377, 1132,
     1240, 1563, 611, 1564, 699, 718, 1870, 963, 1133, 1055, 331, 140, 1457,
     820, 1925, 1850, 1103, 1851, 876, 477, 1395, 19, 1803, 1895, 511, 1579,
     1886, 853, 1181, 155, 489, 965, 573, 590, 1663, 361, 738, 1911, 962, 473,
     875, 1110, 772, 715, 346, 1764, 1012, 1977, 682, 446, 480, 894, 393, 188,
     481, 37, 1244, 861, 1825, 1374, 1316, 1031, 93, 1656, 1357, 289, 1310, 93,
     296, 1235, 158, 580, 1191, 1984, 1352, 1334, 831, 377, 130, 361, 2024,
     659, 1213, 1359, 1288, 1894, 1708, 346, 1407, 1366, 1631, 1913, 1839, 872,
     583, 1917, 1068, 1256, 651, 767, 1756, 1772, 1056, 634, 1688, 507, 1479,
     1717, 1959, 416, 1859, 1493, 680, 1536, 2006, 119, 30, 1636, 1732, 407,
     472, 1698, 1201, 1671, 184, 1727, 1707, 99, 1859, 1423, 261, 477, 654,
     1025, 1466, 765, 10, 90, 428, 210, 1158, 1223, 954, 101, 1200, 565, 446,
     1316, 325, 413, 1978, 1972, 1670, 681, 541, 1864, 1559, 98, 239, 1485,
     1013, 1063, 619, 1572, 599, 1580, 64, 1307, 1239, 1959, 744, 1695, 1328,
     1461, 1931, 1413, 251, 277, 1794, 1844, 855, 265, 1120, 13, 1147, 349,
     1473, 1442, 764, 1918, 645, 1173, 1665, 124, 1827, 671, 872, 18, 1095,
     1192, 1985, 831, 965, 1995, 456, 361, 410, 1997, 1487, 1077, 620, 804,
     1370, 1174, 297, 370, 1406, 716, 1368, 817, 1328, 168, 923, 1271, 1650,
     887, 1360, 96, 1786, 957, 1034, 442, 814, 121, 406, 1491, 141, 687, 1884,
     568, 359, 1337, 615, 853, 1989, 1866, 580, 1763, 1530, 160, 1897, 499, 12,
     481, 1689, 0, 129, 1714, 1041, 402, 446, 1027, 183, 1678, 1123, 1304, 464,
     961, 569, 1813, 2008, 1990, 451, 1738, 1600, 310, 39, 312, 1971, 1044,
     1518, 1901, 1562, 1860, 732, 1622, 1137, 1029, 831, 2003, 432, 747, 1030,
     1473, 1380, 854, 515, 1998, 1012, 508, 1848, 1386, 1248, 1887, 769, 1387,
     832, 1372, 657, 1861, 1933, 873, 1282, 1379, 61, 52, 1512, 1453, 543, 602,
     568, 1751, 1298, 828, 109, 349, 331, 1439, 1327, 774, 15, 670, 535, 708,
     540, 1717, 1251, 1275, 1538, 895, 1140, 1062, 1274, 704, 1230, 206, 413,
     1055, 1712, 1869, 347, 1400, 797, 905, 1967, 1353, 1814, 1514, 1637, 667,
     1551, 2, 720, 552, 1123, 1316, 927, 314, 87, 1710, 1813, 1574, 1935, 249,
     1082, 223, 1064, 701, 1505, 229, 1789, 386, 1792, 659, 1608, 1330, 1581,
     1051, 428, 1397, 1409, 126, 1522, 1185, 67, 1789, 1587, 385, 1923, 1094,
     962, 1374, 216, 329, 246, 1112, 970, 1921, 1847, 2004, 1113, 988, 1790,
     734, 1517, 329, 1047, 1942, 1269, 651, 1462, 799, 1961, 1039, 1273, 1485,
     527, 468, 1518, 32, 1343, 69, 1288, 733, 474, 1536, 1471, 1786, 28, 19,
     1170, 655, 178, 1753, 704, 1229, 1520, 1711, 949, 945, 797, 914, 811,
     1518, 862, 942, 544, 1182, 1596, 850, 1691, 754, 107, 886, 1876, 14, 513,
     1065, 1274, 1114, 927, 225, 1609, 945, 1503, 1284, 8, 794, 1505, 1401,
     1409, 100, 1336, 1528, 1494, 284, 1945, 995, 1819, 515, 1701, 779, 1575,
     384, 589, 848, 1435, 1225, 1497, 44, 2013, 485, 909, 14, 167, 1516, 1219,
     848, 1983, 67, 1679, 1445, 1009, 659, 313, 589, 1706, 342, 1637, 51, 892,
     522, 1552, 1310, 649, 1641, 973, 805, 1433, 93, 749, 878, 174, 961, 994,
     1132, 1474, 1932, 81, 1845, 103, 202, 883, 641, 2005, 1140, 1276, 1589,
     2012, 953, 673, 623, 1359, 1390, 1262, 959, 1405, 501, 1409, 764, 1005,
     1550, 1637, 1393, 1015, 1728, 271, 781, 781, 1407, 1758, 323, 235, 357,
     1313, 1227, 1845, 1604, 1214, 157, 1264, 939, 1003, 969, 417, 1825, 1024,
     403, 1124, 304, 1752, 985, 929, 771, 1765, 12, 1648, 593, 1191, 1190,
     1652, 1744, 248, 1791, 210, 524, 331, 749, 993, 374, 1822, 459, 1773, 511,
     605, 668, 962, 249, 1496, 675, 2020, 410, 278, 348, 1194, 1577, 1643, 969,
     1303, 1060, 346, 1605, 1001, 1785, 1270, 1064, 1499, 311, 640, 1541, 720,
     485, 1567, 1464, 688, 902, 190, 745, 935, 624, 450, 1641, 1589, 930, 597,
     1929, 1195, 1470, 1106, 1892, 1559, 1281, 850, 1616, 1047, 646, 1337,
     1145, 620, 1488, 326, 1127, 1952, 1412, 866, 1397, 1079, 853, 1227, 441,
     1434, 624, 1635, 803, 482, 1438, 743, 983, 1089, 1201, 1371, 398, 1502,
     1885, 583, 1374, 1640, 1049, 1808, 54, 1872, 850, 1577, 1294, 1890, 99,
     132, 282, 1328, 1754, 464, 1591, 1854, 1933, 874, 1472, 1348, 1340, 276,
     989, 670, 1181, 1634, 1784, 694, 356, 1941, 1624, 1060, 1062, 1602, 1856,
     1170, 1851, 385, 190, 1330, 1253, 859, 1217, 1050, 1305, 1742, 466, 1659,
     1291]

    answer = get_candies(test1)
    assert answer == 1013, 'you dun goofed'

    test2 = [158, 222, 15, 141, 112, 159, 121, 87, 47, 138, 121, 201, 31, 46, 3, 237, 228, 10, 64, 42, 56, 251, 93, 230, 197, 108, 226, 190, 202, 161, 3, 207, 28, 166, 70, 89, 53, 198, 177, 58, 170, 69, 161, 118, 245, 53, 156, 143, 219, 59, 189, 202, 227, 212, 250, 128, 83, 177, 193, 72, 161, 27, 3, 103, 231, 68, 194, 95, 21, 198, 78, 114, 235, 18, 106, 198, 23, 87, 73, 112, 172, 211, 6, 131, 108, 191, 83, 67, 48, 211, 78, 127, 57, 60, 23, 229, 11, 194, 16, 230, 230, 94, 73, 192, 213, 141, 69, 139, 2, 26, 158, 225, 174, 94, 136, 57, 114, 172, 167, 81, 217, 203, 54, 121, 5, 76, 189, 170, 46, 37, 24, 23, 40, 182, 221, 184, 145, 249, 237, 152, 220, 23, 59, 79, 88, 194, 186, 91, 178, 106, 7, 89, 226, 137, 62, 83, 170, 40, 70, 223, 176, 164, 248, 232, 149, 33, 254, 131, 2, 150, 54, 218, 182, 104, 18, 238, 128, 241, 207, 213, 145, 30, 165, 77, 248, 238, 91, 237, 44, 232, 76, 107, 142, 152, 121, 164, 101, 104, 173, 138, 237, 133, 117, 130, 200, 211, 1, 131, 17, 182, 3, 58, 114, 57, 136, 7, 224, 207, 85, 5, 110, 243, 104, 177, 148, 235, 219, 5, 225, 39, 114, 193, 118, 81, 1, 166, 51, 103, 156, 201, 34, 173, 72, 220, 124, 172, 136, 199, 203, 130, 33, 57, 208, 72, 200, 180, 187, 141, 176, 206, 23, 219, 79, 71, 158, 141, 76, 187, 220, 225, 108, 249, 102, 128, 217, 231, 90, 70, 65, 214, 246, 19, 112, 162, 167, 123, 169, 142, 24, 165, 56, 70, 202, 207, 149, 163, 173, 138, 122, 224, 247, 143, 210, 25, 216, 183, 55, 139, 101, 69, 255, 154, 225, 244, 93, 160, 39, 17, 229, 217, 38, 38, 185, 238, 167, 102, 95, 212, 98, 118, 72, 130, 167, 54, 44, 230, 16, 68, 251, 138, 140, 198, 31, 3, 144, 195, 164, 19, 150, 227, 187, 220, 139, 211, 237, 233, 20, 227, 17, 21, 32, 54, 145, 154, 1, 160, 57, 192, 38, 53, 119, 225, 187, 138, 90, 176, 102, 130, 88, 70, 153, 115, 81, 57, 110, 235, 187, 65, 174, 215, 118, 212, 186, 251, 0, 234, 246, 100, 170, 168, 128, 213, 153, 54, 34, 32, 215, 48, 10, 30, 58, 250, 183, 141, 98, 193, 72, 142, 18, 171, 86, 27, 111, 192, 214, 132, 56, 73, 131, 54, 219, 135, 47, 3, 24, 134, 143, 111, 255, 204, 12, 130, 45, 9, 6, 122, 5, 238, 188, 156, 240, 55, 188, 199, 31, 218, 90, 162, 147, 207, 209, 87, 132, 18, 80, 86, 0, 159, 164, 56, 149, 20, 11, 121, 74, 251, 235, 139, 227, 245, 229, 169, 188, 98, 73, 173, 207, 7, 150, 105, 164, 189, 163, 158, 114, 199, 7, 219, 127, 131, 239, 88, 23, 73, 68, 219, 124, 107, 34, 226, 206, 3, 203, 68, 72, 92, 60, 203, 96, 179, 43, 155, 43, 114, 147, 3, 116, 56, 187, 203, 135, 86, 41, 107, 217, 138, 159, 177, 123, 175, 53, 113, 227, 218, 46, 38, 43, 151, 204, 108, 76, 132, 204, 196, 252, 137, 235, 225, 145, 212, 112, 90, 107, 88, 149, 221, 1, 139, 173, 115, 28, 103, 172, 110, 45, 208, 111, 175, 37, 67, 129, 143, 6, 84, 72, 237, 181, 82, 107, 158, 230, 42, 67, 40, 181, 221, 140, 92, 11, 212, 34, 149, 219, 27, 208, 129, 193, 147, 187, 28, 90, 169, 43, 83, 18, 224, 253, 81, 139, 204, 168, 78, 32, 173, 146, 57, 14, 164, 63, 226, 39, 139, 69, 95, 75, 41, 215, 131, 121, 189, 80, 79, 204, 63, 77, 197, 129, 40, 39, 17, 13, 152, 59, 78, 69, 194, 253, 188, 91, 197, 95, 236, 87, 148, 232, 210, 201, 181, 246, 201, 222, 39, 181, 22, 96, 82, 99, 219, 142, 50, 195, 93, 143, 8, 179, 254, 162, 192, 182, 27, 75, 58, 24, 21, 251, 169, 201, 13, 208, 96, 57, 145, 77, 94, 59, 151, 235, 90, 18, 105, 90, 63, 222, 62, 151, 219, 152, 17, 8, 106, 248, 129, 197, 99, 239, 190, 253, 199, 208, 93, 78, 193, 31, 181, 166, 29, 227, 2, 249, 94, 247, 42, 108, 109, 90, 92, 123, 116, 73, 176, 28, 11, 61, 75, 112, 10, 176, 225, 168, 66, 140, 12, 143, 3, 31, 36, 184, 113, 29, 20, 153, 69, 17, 240, 165, 3, 5, 171, 70, 35, 153, 105, 6, 89, 252, 212, 131, 254, 75, 204, 215, 183, 248, 225, 124, 231, 15, 86, 35, 7, 2, 133, 195, 81, 46, 151, 79, 178, 120, 7, 127, 148, 91, 178, 34, 244, 190, 62, 200, 148, 92, 252, 202, 166, 74, 4, 110, 205, 23, 34, 96, 112, 212, 167, 76, 46, 129, 220, 113, 219, 132, 101, 64, 203, 249, 130, 226, 182, 242, 140, 186, 254, 14, 206, 43, 159, 199, 57, 239, 173, 20, 201, 223, 106, 149, 92, 162, 148, 246, 198, 184, 125, 239, 228, 161, 247, 144, 235, 127, 124, 2, 98, 227, 84, 163, 189, 202, 170, 0, 113, 25, 208, 99, 222, 45, 232, 234, 201, 171, 159, 160, 18, 12, 95, 120, 203, 250, 120, 223, 27, 72, 88, 6, 46, 67, 12, 162, 180, 138, 119, 19, 84, 59, 26, 102, 163, 55, 71, 47, 117, 240, 165, 108, 246, 156, 208, 30, 180, 153, 30, 87, 63, 8, 224, 81, 221, 27, 60, 231, 31, 227, 193, 26, 237, 189, 83, 144, 174, 46, 217, 42, 225, 241, 134, 49, 174, 165, 91, 241, 211, 53, 125, 3, 112, 36, 52, 115, 143, 125, 116, 110, 16, 22, 198, 100, 93, 67, 106, 80, 30, 83, 152, 254, 63, 68, 76, 252, 85, 90, 218, 27, 74, 169, 95, 200, 123, 124, 228, 50, 71, 145, 145, 88, 103, 89, 87, 22, 36, 52, 173, 17, 40, 114, 213, 101, 8, 90, 135, 187, 207, 65, 0, 73, 207, 20, 216, 220, 32, 183, 106, 39, 49, 22, 110, 224, 219, 219, 46, 122, 97, 46, 117, 220, 128, 249, 81, 138, 14, 137, 22, 110, 166, 189, 177, 188, 167, 149, 147, 66, 154, 187, 142, 23, 247, 26, 188, 168, 134, 49, 88, 49, 146, 165, 33, 202, 159, 49, 198, 114, 114, 198, 158, 110, 199, 128, 234, 116, 164, 202, 125, 35, 40, 192, 9, 252, 23, 190, 147, 89, 58, 166, 134, 112, 42, 216, 27, 127, 163, 165, 1, 153, 54, 157, 20, 154, 250, 79, 123, 27, 47, 19, 45, 58, 125, 118, 225, 249, 30, 16, 55, 100, 44, 168, 31, 18, 55, 212, 87, 219, 1, 200, 87, 161, 57, 120, 158, 13, 232, 222, 187, 106, 57, 97, 158, 197, 20, 42, 101, 41, 78, 246, 39, 132, 125, 143, 169, 6, 195, 133, 32, 93, 224, 108, 42, 11, 84, 33, 107, 63, 85, 147, 171, 197, 154, 128, 130, 149, 22, 151, 21, 117, 165, 3, 63, 123, 161, 236, 38, 34, 72, 235, 96, 18, 192, 0, 238, 89, 152, 33, 89, 35, 172, 212, 126, 203, 130, 72, 115, 243, 77, 9, 62, 117, 163, 216, 94, 208, 105, 162, 180, 160, 221, 22, 160, 87, 98, 244, 119, 91, 0, 246, 64, 75, 19, 248, 25, 45, 69, 143, 57, 0, 88, 201, 231, 182, 1, 239, 189, 9, 54, 60, 234, 155, 98, 170, 227, 153, 72, 158, 186, 62, 252, 230, 159, 61, 101, 150, 165, 108, 253, 206, 196, 155, 181, 19, 78, 240, 156, 248, 227, 164, 39, 172, 170, 165, 216, 139, 73, 5, 231, 5, 208, 246, 162, 47, 129, 1, 168, 69, 163, 56, 149, 15, 16, 235, 140, 20, 142, 181, 17, 36, 73, 126, 47, 127, 105, 159, 14, 50, 84, 209, 126, 87, 202, 110, 84, 99, 47, 84, 156, 203, 205, 222, 41, 133, 55, 201, 69, 208, 185, 244, 182, 80, 185, 52, 219, 167, 208, 60, 94, 163, 213, 17, 228, 53, 58, 6, 94, 181, 218, 56, 226, 75, 80, 191, 63, 42, 241, 6, 8, 53, 182, 16, 113, 253, 76, 193, 188, 137, 46, 53, 7, 179, 193, 40, 25, 94, 210, 65, 120, 14, 181, 8, 240, 115, 179, 140, 29, 227, 36, 61, 32, 121, 180, 247, 148, 150, 117, 101, 243, 230, 209, 202, 81, 70, 111, 188, 252, 17, 99, 118, 171, 167, 222, 211, 155, 195, 122, 5, 102, 159, 162, 122, 113, 0, 101, 171, 253, 50, 62, 61, 250, 192, 33, 151, 131, 110, 197, 60, 212, 89, 86, 111, 30, 69, 81, 131, 49, 138, 75, 39, 108, 248, 21, 12, 70, 111, 71, 30, 249, 107, 58, 88, 168, 175, 146, 2, 1, 54, 179, 226, 53, 127, 203, 178, 97, 134, 28, 155, 2, 220, 22, 58, 102, 186, 77, 46, 71, 243, 192, 96, 158, 245, 215, 10, 186, 156, 62, 251, 226, 230, 12, 212, 87, 216, 241, 87, 49, 106, 191, 234, 242, 171, 192, 237, 193, 32, 233, 13, 72, 103, 182, 228, 97, 69, 32, 144, 116, 27, 51, 80, 129, 239, 84, 242, 191, 99, 98, 109, 15, 211, 243, 31, 196, 141, 118, 110, 136, 32, 216, 156, 207, 125, 69, 97, 201, 224, 220, 205, 68, 215, 38, 226, 71, 13, 22, 138, 242, 194, 45, 4, 176, 233, 116, 171, 231, 247, 179, 162, 94, 191, 210, 211, 135, 11, 31, 175, 22, 125, 146, 134, 137, 67, 159, 229, 46, 133, 219, 159, 12, 191, 234, 226, 220, 102, 127, 20, 100, 99, 105, 74, 26, 35, 217, 109, 102, 191, 172, 87, 6, 184, 78, 162, 46, 208, 117, 112, 13, 252, 11, 99, 102, 28, 216, 243, 192, 86, 156, 102, 49, 162, 235, 18, 126, 210, 160, 244, 220, 28, 203, 246, 224, 245, 157, 15, 213, 247, 178, 149, 176, 208, 227, 169, 156, 225, 95, 79, 227, 31, 186, 220, 184, 191, 22, 157, 114, 242, 63, 168, 36, 171, 249, 226, 53, 201, 108, 183, 18, 26, 4, 119, 215, 61, 115, 78, 131, 14, 65, 95, 251, 135, 165, 58, 132, 98, 76, 158, 75, 10, 12, 140, 230, 190, 150, 10, 153, 96, 41, 16, 130, 13, 80, 66, 79, 207, 250, 63, 179, 90, 243, 144, 17, 66, 215, 57, 200, 225, 217, 78, 30, 197, 121, 147, 122, 166, 116, 12, 16, 190, 34, 6, 212, 148, 82, 79, 198, 126, 199, 164, 188, 8, 155, 51, 218, 226, 130, 120, 123, 30, 8, 41, 253, 138, 128, 254, 101, 15, 131, 83, 254, 26, 122, 7, 196, 27, 144, 146, 61, 114, 221, 186, 134, 212, 222, 66, 94, 76, 25, 201, 94, 111, 228, 253, 9, 17, 232, 58, 101, 34, 169, 124, 57, 69, 254, 121, 147, 52, 140, 253, 227, 208, 4, 85, 165, 244, 77, 12, 8, 169, 34, 215, 228, 125, 84, 220, 169, 92, 227, 185, 146, 3, 247, 56, 218, 214, 9, 20, 89, 185, 169, 31, 124, 247, 203, 249, 24, 53, 0, 85, 246, 235, 48, 236, 133, 249, 9, 5, 70, 166, 253, 49, 3, 123, 169, 44, 237, 102, 100, 209, 165, 71, 80, 180, 23, 153, 227, 130, 70, 55, 248, 161, 111, 14, 96, 108, 123, 13, 246, 244, 153, 1, 37, 53, 62, 165, 74, 212, 241, 195, 6, 102, 246, 43, 125, 241, 53, 93, 53, 79, 123, 251, 110, 75, 168, 232, 85, 63, 42, 243, 239, 90, 197, 16, 248, 69, 119, 220, 85, 159, 105, 67, 208, 35, 130, 25, 169, 7, 82, 48, 114, 182, 208, 82, 199, 113, 220, 137, 26, 48, 133, 19, 5, 241, 202, 195, 63, 58, 74, 59, 184, 7, 228, 17, 179, 98, 81, 60, 132, 70, 12, 227, 51, 112, 49, 60, 43, 221, 109, 85, 100, 163, 180, 184, 232, 212, 49]
    answer = get_candies(test2)
    assert answer == 256, 'you dun goofed'


def main():
    example = [1,1,2,2,3,3]
    # example = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    answer = get_candies(example)
    assert answer == 3, 'you dun goofed'

    t = timeit.Timer(test)
    print(t.timeit(200)/100)



if __name__ == '__main__':
    main()