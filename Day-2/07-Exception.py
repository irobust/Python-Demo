""" Exception hadling demonstrartion
"""
def doError():
    """
        make error happen

        Args:
            x: .....
        
        Returns:
            No return
        
        Raises:
            KeyError: if key not exist
            IndexError: if index out of bound
            ValueError: if value mismatch
    """
    data = dict(a=10, b=20)
    listData = [1,2,3,4]

    try:
        # KeyError
        # print(data['c'])

        # IndexError
        # print(listData[4])

        # ValueError
        int('one')
    except (KeyError, IndexError, ValueError) as e:
        print(f'Some error happen: {e!r}')
    finally:
        print('Finished program')

if(__name__ == '__main__'): doError()