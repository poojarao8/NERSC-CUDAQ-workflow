import cudaq

cudaq.set_target("nvidia", option="mgpu")

def ghz_state(N):

    kernel = cudaq.make_kernel()
    q = kernel.qalloc(N)

    kernel.h(q[0])
    for i in range(N - 1):
      kernel.cx(q[i], q[i + 1])

    kernel.mz(q)
    return kernel

n = 34
print("Preparing GHZ state for", n, "qubits.")
kernel = ghz_state(n)
counts = cudaq.sample(kernel)
counts.dump()
