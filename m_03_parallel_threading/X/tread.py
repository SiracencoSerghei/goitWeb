from pathlib import Path
from threading import Thread, Semaphore
import sys
import logging
import shutil


def get_dirs():
    try:
        dirs = list(Path(sys.argv[1]).glob("*"))
        dirs.append(Path(sys.argv[1]))
        return dirs
    except IndexError:
        print("No path to folder")
    exit()


def threads_dividing(dirs):
    semaphore = Semaphore(2)
    for one_dir in dirs:
        Thread(
            name= one_dir, 
            target=sorting_files, 
            args=(one_dir, semaphore),
            ).start()
        
    
def sorting_files(one_dir, semaphore):
    with semaphore:
        logging.debug("start")
        for el in one_dir.glob("**/*"):
            dist = el.suffix[1:] if el.suffix else "unknown"
            if one_dir == Path(sys.argv[1]):
                target_dir = one_dir / dist
            else:
                target_dir = one_dir.parent / dist
            target_file = target_dir / el.name
            if el.is_file():
                target_dir.mkdir(parents=True, exist_ok=True)
                counter = 1
                while target_file.exists():
                    target_file = target_dir / f"{el.stem}_{counter}{el.suffix}"
                    counter += 1
                shutil.move(str(el), str(target_file))
        logging.debug("finished")
        

def main():
    logging.basicConfig(
        level=logging.DEBUG, 
        format="%(asctime)s %(threadName)s %(message)s", 
        datefmt="%M:%S"
        )
    dirs_to_sortout = get_dirs()

    threads_dividing(dirs_to_sortout) 


if __name__ == "__main__":
    main()
   