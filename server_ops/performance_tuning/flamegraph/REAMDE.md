# Flame Graph

Flame graphs are a visualization of hierarchical data, created to visualize stack traces of profiled software so that the most frequent code-paths to be identified quickly and accurately.

Basically, it is known as a visualizer of the stack trace.

This was created by `Brendan Gregg`, and you could learn more about the flame graph from [here](https://www.brendangregg.com/flamegraphs.html)

- [Github Repo of FlameGraph](https://github.com/brendangregg/FlameGraph)
- [d3 version of flame graph](https://github.com/spiermar/d3-flame-graph)

## FlameGraphs in Python

There are several ways to generate flame graphs in python.
Personally, I prefer using `py-spy` the most, since it is easy to use and the most intuitive tool.

- [py-spy](https://github.com/benfred/py-spy)
- [flask flamegraph](https://github.com/schireson/flask-flamegraph)
- [python-benchmark-harness](https://github.com/JoeyHendricks/python-benchmark-harness)
    * [Reddit Post of using flamegraphs for python](https://www.reddit.com/r/Python/comments/mzaixf/this_is_how_you_can_generate_flame_graphs_from/)

## FlameGraphs for Node.js

- [ndoe flame graphs on linux](https://www.brendangregg.com/blog/2014-09-17/node-flame-graphs-on-linux.html)

## References

- [Reddit Post of using flamegraphs for python](https://www.reddit.com/r/Python/comments/mzaixf/this_is_how_you_can_generate_flame_graphs_from/)
- [Brendan Gregg's blog about flamegraphs](https://www.brendangregg.com/flamegraphs.html)
