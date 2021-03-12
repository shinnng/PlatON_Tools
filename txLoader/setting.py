from client_sdk_python import Web3, HTTPProvider, WebsocketProvider


# 链设置
rpc = 'ws://192.168.120.121:6788'
# rpc = 'http://192.168.120.121:6789'
chain_id = 201018
web3 = Web3(HTTPProvider(rpc), chain_id=chain_id)

# 压测设置
load_threads = 1                                                    # 压测线程数
load_accounts = 1                                                   # 每个线程使用账户数
load_duration = 60                                                 # 压测时长/s
load_amount = 2000                                                  # 压测账户的初始金额
load_funcs = ['delegate', 'undelegate', 'withdraw_reward']          # 需要压测的请求,从action中选择
load_ratios = [7, 0, 0]                                             # 压测请求的发送比率
# is_hold_nonce = True  # todo: coding

# 账户设置
main_address, main_private_key = 'lat1rzw6lukpltqn9rk5k59apjrf5vmt2ncv8uvfn7', 'f90fd6808860fe869631d978b0582bb59db6189f7908b578a886d582cb6fccfa'
main_nonce = web3.platon.getTransactionCount(main_address)
cdf_address, cdf_private_key = 'lat1kvurep20767ahvrkraglgd9t34w0w2g059pmlx', 'f767d379a652ab5cc8c85cd7fef1b00bffcec90697dcfd6c64991dd284cac4e9'