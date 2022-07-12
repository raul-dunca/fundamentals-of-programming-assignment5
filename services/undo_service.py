class UndoServiceExc(Exception):
    pass

class UndoService:

    def __init__(self):
        self._history = []
        self._index = -1
        self._counter=0

    def record(self, operation):
       # self._count+=1

        if self._counter>0:
            self._counter=0
            del self._history[self._index+1]
        self._history.append(operation)
        self._index = len(self._history)-1
       # if self._count >= 2:
       #     del self._history[self._index-1]
       #     self._index-=1


    def undo(self):

        if self._index == -1:
            raise UndoServiceExc("No more undos")
        self._counter+=1
        self._history[self._index].undo()
        self._index -= 1

    def redo(self):
        if self._index+1 >= len(self._history):
            raise UndoServiceExc("No more redos")
        self._counter-=1
        self._index+=1
        self._history[self._index].redo()



class Call:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        self._function_name(*self._function_params)


'''
    private ArrayList<Operation> history;
'''


class Operation:
    def __init__(self, undo_call, redo_call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        self._undo_call.call()

    def redo(self):
        self._redo_call.call()


class CascadedOperation:
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):

        for oper in self._operations:
            oper.undo()

    def redo(self):
        for oper in self._operations:
            oper.redo()