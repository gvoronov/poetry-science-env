import subprocess

def main():
    get_process_id_cmd = (
        "sudo lsof /dev/nvidia* | awk '$3 == \"gennady.voronov\" "
        "{print $2 }' | sort | uniq"
    )
    out = subprocess.run(get_process_id_cmd, capture_output=True, shell=True)
    
    kill_cuda_procs_cmd = (
        "kill -9 " + out.stdout.decode().rstrip("\n").replace("\n", " ")
    )
    subprocess.run(kill_cuda_procs_cmd, shell=True)

if __name__ == "__main__":
    main()
