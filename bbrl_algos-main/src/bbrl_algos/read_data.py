

input_dqn_file = "E:/sorbonne/IAR/mini_projet_nouveau/bbrl_algos-main/src/bbrl_algos/algos/dqn/tmp/hydra/2023-10-30/15-04-51/dqn_data/dqn_LunarLander-v2.data"
output_dqn_file = "E:/sorbonne/IAR/mini_projet_nouveau/bbrl_algos-main/src/bbrl_algos/algos/dqn/tmp/hydra/2023-10-30/15-04-51/dqn_data/dqn_LunarLander-v2.txt"

input_ddqn_file = "E:/sorbonne/IAR/mini_projet_nouveau/bbrl_algos-main/src/bbrl_algos/algos/ddqn/tmp/hydra/2023-10-30/16-10-09/dqn_data/dqn_LunarLander-v2.data"
output_ddqn_file = "E:/sorbonne/IAR/mini_projet_nouveau/bbrl_algos-main/src/bbrl_algos/algos/ddqn/tmp/hydra/2023-10-30/16-10-09/dqn_data/ddqn_LunarLander-v2.txt"
with open(input_dqn_file) as f:
    data = f.read()
    #data = data.split("\n")
    #for line in data:
        #print(line)

with open(output_dqn_file, "w") as f:
    f.write(data)

with open(input_ddqn_file) as f:
    data = f.read()
    #data = data.split("\n")
    #for line in data:
        #print(line)
with open(output_ddqn_file, "w") as f:
    f.write(data)

