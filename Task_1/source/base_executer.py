import abc

class BaseExecuter(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass