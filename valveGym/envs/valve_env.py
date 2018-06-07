import gym
from gym import error,spaces,utils
from gym.utils import seeding
import numpy as np
from mpi4py import MPI

class ValveEnv(gym.Env):
  metadata={'render.modes':['human']}
  def __init__(self):
    self.comm=MPI.COMM_WORLD
    self.rank=self.comm.Get_rank()
    self.status=MPI.Status()
    self.action_space=spaces.Box(low=np.array([0,0]),high=np.array([2,20000]))
    self.state_space=spaces.Box(low=np.array([0,310]),high=np.array([2,20000]))
  def step(self,action):
    assert self.action_space.contains(action)

    self.comm.Send(action,partner,tag=1)

    data=np.zeros((4,))
    self.comm.Recv(data,status=status)
    state=data[:2]
    reward=data[2]
    done=((data[3]-1.0)>-.001)
    
    return state,reward,done,None


  def reset(self):
    data=np.zeros((4,))
    self.comm.Recv(data,status=status)
    state=data[:2]
    return state

  def render(self,mode='human',close=False):
    pass
  def seed(self):
    pass
