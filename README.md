# stream_gym
Data Stream Gym for Reinforcement Learning | Stock Market, TimeSeries Data

When we going to develop RL algorithms for stream time series datasets like Stock Market, Forex we need a simple way to manage environment like openai gym. This simple code is help you to start your own openai gym for time series data for streaming data sets

### Here is the magic happen

```python

env = FxDataEnvironment(data_csv.Close.values, data_frame_size, k_steps=k_steps)

state = env.reset()
done = False
action = np.array([0, 0, 0, 0, 0, 0, 1])
while done is False:
    next_state, reward, done = env.step(action)
    print(f" state - {state}, next state -{next_state}, reward - {reward}, done status - {done}")
    if done:
        print(f"end session {next_state},{state}")
    state = next_state

```


##  This is the Class what we act as a Environment
```python
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



```
## This is the Simple implimentation 

You can use any data stream pass this

```python

class FxDataEnvironment(EnvPlay):

    def __init__(self, data_stream, data_frame_size=1, k_steps=1):
        super().__init__()
        self.k_steps = k_steps
        self.data_frame_size = data_frame_size
        self.state_min_size = data_frame_size
        self.data_stream = data_stream

    def __get_first_state__(self):
        return self.data_stream[self.cur_time_step:self.cur_time_step + self.data_frame_size]

    def __get_next_state__(self, k_steps=1):
        return self.data_stream[self.cur_time_step + k_steps:self.cur_time_step + k_steps + self.data_frame_size]

    def __reward__(self, action, state):
        return 1

    def __after_init__(self):
        pass

    def __finalize_process__(self):
        # print(self.data_stream[-6:])
        pass

```



Simply You run above example



## How to use

```python
   python ForexMarketEnv.py
```



# Here is the results for the testing results from different configurations.

## Test 1

### Config
```python
   
   data_frame_size = 1
   k_steps = 1
```
### Result
![GitHub Logo](https://raw.githubusercontent.com/ceylonai/stream_gym/master/image.png)




## Test 2

### Config
```python
   
   data_frame_size = 1
   k_steps = 2
```
### Result
![GitHub Logo](https://raw.githubusercontent.com/ceylonai/stream_gym/master/result1.png)


## Test 3

### Config
```python
   
   data_frame_size = 2
   k_steps = 1
```
### Result
![GitHub Logo](https://raw.githubusercontent.com/ceylonai/stream_gym/master/result2.png)



## Test 3

### Config
```python
   
   data_frame_size = 3
   k_steps = 2
```
### Result
![GitHub Logo](https://raw.githubusercontent.com/ceylonai/stream_gym/master/result3.png)
