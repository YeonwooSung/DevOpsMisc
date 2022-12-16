# use "quantize()" to show the distribution of read() sizes by print out quantized histogram of the read() sizes of all processes
# basically, the arg0 in this example is the return value of read() syscall
dtrace -n 'syscall::read:entry { @["size"] = quantize(arg0); }'
