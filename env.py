from abc import abstractmethod, ABC


class EnvPlay(ABC):
    action_space = None
    observation_space = None
    __state__ = None
    state_min_size = 0
    k_steps = 1
    cur_time_step = 0

    def __init__(self):
        self.__after_init__()

    def reset(self):
        return self.__get_first_state__()

    def step(self, action):
        next_state = self.__get_next_state__(self.k_steps)
        reward = self.__reward__(action, next_state)
        done = True if next_state is None or len(next_state) != self.state_min_size else False
        self.cur_time_step += self.k_steps
        if done:
            self.__finalize_process__()
        return next_state, reward, done

    @abstractmethod
    def __get_first_state__(self):
        '''
        Implement get first state
        :return:
        '''
        pass

    @abstractmethod
    def __get_next_state__(self, k_steps=1):
        '''
        Implement get Next State Function
        :param k_steps:
        :return:
        '''
        pass

    @abstractmethod
    def __reward__(self, action, state):
        '''
        Implement Reward Function
        :param action:
        :param state:
        :return:
        '''
        pass

    @abstractmethod
    def __after_init__(self):
        '''
        Implement After init function
        This method call in __init__

        '''
        pass

    @abstractmethod
    def __finalize_process__(self):
        '''
        Call On Last State
        '''
        pass
