import pandas as pd


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
        
        
        
        
if __name__ == 'main':

  data_csv = pd.read_csv('file_name')

  env = FxDataEnvironment(data_csv.Close.values, data_frame_size, k_steps=k_steps)

  state = env.reset()
  done = False
  action = np.array([0, 0, 0, 0, 0, 0, 1])
  while done is False:
      next_state, reward, done = env.step(action)
      if done:
          print(f"end session {next_state},{state}")
      state = next_state
