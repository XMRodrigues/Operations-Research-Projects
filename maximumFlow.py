from __future__ import print_function
from ortools.graph import pywrapgraph
  
  #First Operations Research Project (19/07/2020)
  
def main():

  #This code was based upon Maximum Flow section at Or-Tools guide provided by Google
  #Source: https://developers.google.com/optimization/flow/maxflow
  
  start_nodes = [0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9]
  end_nodes = [1, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9, 8, 9, 10, 10, 10]
  capacities = [245, 270, 260, 130, 115, 70, 90, 110, 140, 120, 110, 85, 130, 95, 85, 130, 160, 220, 330, 240]

  max_flow = pywrapgraph.SimpleMaxFlow()
  for i in range(0, len(start_nodes)):
    max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])

  if max_flow.Solve(0, 10) == max_flow.OPTIMAL:
    print('Max flow:', max_flow.OptimalFlow())
    print('')
    print('  Arc    Flow / Capacity')
    for i in range(max_flow.NumArcs()):
      print('%1s -> %1s   %3s  / %3s' % (
          max_flow.Tail(i),
          max_flow.Head(i),
          max_flow.Flow(i),
          max_flow.Capacity(i)))
    print('Source side min-cut:', max_flow.GetSourceSideMinCut())
    print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
  else:
    print('There was an issue with the max flow input.')

if __name__ == '__main__':
  main()
