try:
    import parasail
except ImportError:
    import sys, os
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../')
    import parasail

def test1():
    matrix = parasail.blosum62
    matrix[3,4] = 100
    print(matrix.matrix)

    matrix = parasail.blosum62.copy()
    matrix[3,4] = 100
    print(matrix.matrix)

    matrix = parasail.matrix_create("ACGT", 10, 1)
    matrix[2] = 200
    matrix[1:3, 1:3] = 300
    matrix.set_value(0,4,400)
    print(matrix.matrix)

    matrix = parasail.matrix_create("AcgT", 10, 1)
    print(matrix.matrix)
    print(matrix.mapper)

    matrix = parasail.matrix_create("AcgT", 10, 1, True)
    print(matrix.matrix)
    print(matrix.mapper)

if __name__ == '__main__':
    print("running tests")
    test1()
