import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description="see running CUDA processes")
    parser.add_argument("--user", type=str, default="")
    parser.add_argument("--kill", action="store_true", type=bool, default=False)
    args = parser.parse_args()
    print(args)

    get_process_id_cmd = (
        f"sudo lsof /dev/nvidia* | awk '$3 == \"{args.user}\" {{print $2}}' | sort | uniq"
    )
    out = subprocess.run(get_process_id_cmd, capture_output=True, shell=True)

    # if args.kill:
    #     kill_cuda_procs_cmd = (
    #         "kill -9 " + out.stdout.decode().rstrip("\n").replace("\n", " ")
    #     )
    #     _ = subprocess.run(kill_cuda_procs_cmd, shell=True)

if __name__ == "__main__":
    main()
