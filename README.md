# Process Synchronization
In this code reader-writter synchronization is implemented using semaphores.

## Working
If one of the people tries editing the file, no other person should be reading or writing at the same time. However if some person is reading the file, then others may read it at the same time.

•	One set of data is shared among a number of processes.

•	Once a writer is ready, it performs its write. Only one writer may write at a time.

•	If a process is writing, no other process can read it.

•	If at least one reader is reading, no other process can write.

•	Readers may not write and only read.
