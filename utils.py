import os


def setup_environment():
    set_env_vars(env_file='.env')

    dir_path = 'configs/env'
    if os.getenv('APP_ENV') == 'dev':
        env_file = f'{dir_path}/dev.env'
    elif os.getenv('APP_ENV') == 'staging':
        env_file = f'{dir_path}/staging.env'
    elif os.getenv('APP_ENV') == 'live':
        env_file = f'{dir_path}/live.env'
        print("***Warning, we are running against live data***")
    else:
        print(f"Invalid APP_ENV of {os.getenv('APP_ENV')}")
        exit(-1)

    set_env_vars(env_file=env_file)
    
    
def set_env_vars(env_file='.env'):
    with open(env_file) as env_file:
        print(f"{env_file} file read.")
        for line in env_file:
            line = line.strip()
            if line == '':
                continue
            if line[0] == '#':
                continue
            if '=' not in line:
                continue
            env_var_list = line.split("=")
            env_var_name = env_var_list[0]
            env_var_val = env_var_list[1]
            os.environ[env_var_name] = env_var_val
            
            
setup_environment()


if __name__ == '__main__':
  print("Starting Script")
  
  print("Ending Script")
