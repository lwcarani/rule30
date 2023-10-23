# rule30

## About
Rule 30 is one of the elementary cellular automaton rules introduced by Stephen Wolfram in 1983. It specifies the next color in a cell, depending on its color, and its immediate neighbors ([Source](https://mathworld.wolfram.com/Rule30.html)). 

The formula is `[left_cell XOR (central_cell OR right_cell)]`. It is called Rule 30 because in binary `00011110 = 30` ([Source](https://en.wikipedia.org/wiki/Rule_30)).

This version is written in Python. 

## Examples
Running for 5 steps:

```console
PS C:\...\rule30> python cli.py --np --steps 5
Running Rule 30 cellular automaton for 5 steps (using a Python implementation with NumPy)
     █
    ███
   ██  █
  ██ ████
 ██  █   █
 █ ████ ██
```
10 steps:

```console
PS C:\...\rule30> python cli.py --np --steps 10
Running Rule 30 cellular automaton for 10 steps (using a Python implementation with NumPy)
          █
         ███
        ██  █
       ██ ████
      ██  █   █
     ██ ████ ███
    ██  █    █  █
   ██ ████  ██████
  ██  █   ███     █
 ██ ████ ██  █   ███
 █  █    █ ████ ██
```
20 steps:

```console
PS C:\...\rule30> python cli.py --np --steps 20
Running Rule 30 cellular automaton for 20 steps (using a Python implementation with NumPy)
                    █
                   ███
                  ██  █
                 ██ ████
                ██  █   █
               ██ ████ ███
              ██  █    █  █
             ██ ████  ██████
            ██  █   ███     █
           ██ ████ ██  █   ███
          ██  █    █ ████ ██  █
         ██ ████  ██ █    █ ████
        ██  █   ███  ██  ██ █   █
       ██ ████ ██  ███ ███  ██ ███
      ██  █    █ ███   █  ███  █  █
     ██ ████  ██ █  █ █████  ███████
    ██  █   ███  ████ █    ███      █
   ██ ████ ██  ███    ██  ██  █    ███
  ██  █    █ ███  █  ██ ███ ████  ██  █
 ██ ████  ██ █  ██████  █   █   ███ ████
 █  █   ███  ████     ████ ███ ██   █
```
And finally, 50 steps:

```console
PS C:\...\rule30> python cli.py --np --steps 50
Running Rule 30 cellular automaton for 50 steps (using a Python implementation with NumPy)
                                                  █
                                                 ███
                                                ██  █
                                               ██ ████
                                              ██  █   █
                                             ██ ████ ███
                                            ██  █    █  █
                                           ██ ████  ██████
                                          ██  █   ███     █
                                         ██ ████ ██  █   ███
                                        ██  █    █ ████ ██  █
                                       ██ ████  ██ █    █ ████
                                      ██  █   ███  ██  ██ █   █
                                     ██ ████ ██  ███ ███  ██ ███
                                    ██  █    █ ███   █  ███  █  █
                                   ██ ████  ██ █  █ █████  ███████
                                  ██  █   ███  ████ █    ███      █
                                 ██ ████ ██  ███    ██  ██  █    ███
                                ██  █    █ ███  █  ██ ███ ████  ██  █
                               ██ ████  ██ █  ██████  █   █   ███ ████
                              ██  █   ███  ████     ████ ███ ██   █   █
                             ██ ████ ██  ███   █   ██    █   █ █ ███ ███
                            ██  █    █ ███  █ ███ ██ █  ███ ██ █ █   █  █
                           ██ ████  ██ █  ███ █   █  ████   █  █ ██ ██████
                          ██  █   ███  ████   ██ █████   █ █████ █  █     █
                         ██ ████ ██  ███   █ ██  █    █ ██ █     █████   ███
                        ██  █    █ ███  █ ██ █ ████  ██ █  ██   ██    █ ██  █
                       ██ ████  ██ █  ███ █  █ █   ███  ████ █ ██ █  ██ █ ████
                      ██  █   ███  ████   ████ ██ ██  ███    █ █  ████  █ █   █
                     ██ ████ ██  ███   █ ██    █  █ ███  █  ██ ████   ███ ██ ███
                    ██  █    █ ███  █ ██ █ █  █████ █  ██████  █   █ ██   █  █  █
                   ██ ████  ██ █  ███ █  █ ████     ████     ████ ██ █ █ █████████
                  ██  █   ███  ████   ████ █   █   ██   █   ██    █  █ █ █        █
                 ██ ████ ██  ███   █ ██    ██ ███ ██ █ ███ ██ █  █████ █ ██      ███
                ██  █    █ ███  █ ██ █ █  ██  █   █  █ █   █  ████     █ █ █    ██  █
               ██ ████  ██ █  ███ █  █ ████ ████ █████ ██ █████   █   ██ █ ██  ██ ████
              ██  █   ███  ████   ████ █    █    █     █  █    █ ███ ██  █ █ ███  █   █
             ██ ████ ██  ███   █ ██    ██  ███  ███   ██████  ██ █   █ ███ █ █  ████ ███
            ██  █    █ ███  █ ██ █ █  ██ ███  ███  █ ██     ███  ██ ██ █   █ ████    █  █
           ██ ████  ██ █  ███ █  █ ████  █  ███  ███ █ █   ██  ███  █  ██ ██ █   █  ██████
          ██  █   ███  ████   ████ █   ██████  ███   █ ██ ██ ███  ██████  █  ██ █████     █
         ██ ████ ██  ███   █ ██    ██ ██     ███  █ ██ █  █  █  ███     ██████  █    █   ███
        ██  █    █ ███  █ ██ █ █  ██  █ █   ██  ███ █  ██████████  █   ██     ████  ███ ██  █
       ██ ████  ██ █  ███ █  █ ████ ███ ██ ██ ███   ████         ████ ██ █   ██   ███   █ ████
      ██  █   ███  ████   ████ █    █   █  █  █  █ ██   █       ██    █  ██ ██ █ ██  █ ██ █   █
     ██ ████ ██  ███   █ ██    ██  ███ ███████████ █ █ ███     ██ █  █████  █  █ █ ███ █  ██ ███
    ██  █    █ ███  █ ██ █ █  ██ ███   █           █ █ █  █   ██  ████    ██████ █ █   ████  █  █
   ██ ████  ██ █  ███ █  █ ████  █  █ ███         ██ █ █████ ██ ███   █  ██      █ ██ ██   ███████
  ██  █   ███  ████   ████ █   ██████ █  █       ██  █ █     █  █  █ █████ █    ██ █  █ █ ██      █
 ██ ████ ██  ███   █ ██    ██ ██      █████     ██ ███ ██   ████████ █     ██  ██  ████ █ █ █    ███
 █  █    █ ███  █ ██ █ █  ██  █ █    ██    █   ██  █   █ █ ██        ██   ██ ███ ███    █ █ ██  ██
```

Beautiful!

## Notes
The above examples were all generated based on my implementation using numpy. I also implemented Rule 30 more naively (un-vectorized) using native Python data structures and libraries, which can be called with the `--naive` flag:

```console
PS C:\...\rule30> python cli.py --naive --steps 10
Running Rule 30 cellular automaton for 10 steps (using a naive Python implementation)
          █
         ███
        ██  █
       ██ ████
      ██  █   █
     ██ ████ ███
    ██  █    █  █
   ██ ████  ██████
  ██  █   ███     █
 ██ ████ ██  █   ███
██  █    █ ████ ██
```

## Acknowledgements
I learned about Rule 30 for the first time a few weeks when I was listening to Lex Fridman interview Stephen Wolfram on Lex's podcast ([I highly recommend a listen!](https://www.youtube.com/watch?v=PdE-waSx-d8)).

Feedback, bug reports, issues, and pull requests welcome!
