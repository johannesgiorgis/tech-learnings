# Threading vs Multiprocessing in Python

- <https://www.youtube.com/watch?v=ecKWiaHCEKs>

Threading:

- A new thread is spawned within the existing process
- Starting a thread is faster than starting a process
- Memory is shared between all threads
- Mutexes often necessary to control access to shared data
- One GIL (Global Interpreter Lock) for all threads

Multiprocessing:

- A new process is started independent from the first process
- Starting a process is slower than starting a thread
- Memory is not shared between processes
- Mutexes not necessary (unless threading in the new process)
- One GIL (Global Interpreter Lock) for each process

Compare `threads.py` vs `processes.py`

When to use one over the other?

**Threading**: Run an e-commerce website selling t-shirts. When someone orders, at least 3 things happen

- Charge the card
- Log all the information to database
- Send email receipt

Charing a card, sending an email take a few seconds each. If card transaction succeeds, why not take the portion where it sends an email and put it in a seperate thread? This way, you can inform the user the order was successful while in the background the email is being sent. How can we do 2 things at the same time with threading? Threading cannot do things in parallel, it can do things concurrently - it can go back and forth between threads when it has the time. Email sending will get to network request phase, the GIL is released for that operation and allowed to go back to telling the user the order was successful. Once the email is sent successfully, the GIL is re-acquired by that thread and the rest of the operation finishes.

**Multiprocessing**: Imagine you have to do some mathematical operations on 2 million records of data. You can divide all that data up for each core and process it independently. E.g. for 32 cores, you can do 1/32nd of the work per process, then use `process.join()` to wait for all the results and aggregate them. That should speed up what you are doing by a factor of 32.
