import subprocess

def main():
    get_process_id_cmd = (
        "sudo lsof /dev/nvidia* | awk '$3 == \"gennady.voronov\" "
        "{print $2 }' | sort | uniq"
    )
    _ = subprocess.run(get_process_id_cmd, shell=True)

if __name__ == "__main__":
    main()
