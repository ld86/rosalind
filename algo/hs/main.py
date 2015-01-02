import sys


def add(heap, a):
    heap.append(a)
    c = len(heap) - 1
    while c != 0:
        p = (c - 1) / 2
        if heap[p] >= heap[c]:
            break
        heap[p], heap[c] = heap[c], heap[p]
        c = p


def sift_down(heap, size):
    root = 0
    while root < size:
        l = 2 * root + 1
        r = 2 * root + 2

        if l >= size or r >= size:
            break

        if heap[root] >= heap[l] and heap[root] >= heap[r]:
            break

        if heap[l] < heap[r]:
            heap[root], heap[r] = heap[r], heap[root]
            root = r
        else:
            heap[root], heap[l] = heap[l], heap[root]
            root = l


def hs(heap):
    last = len(heap) - 1
    while last != 0:
        heap[last], heap[0] = heap[0], heap[last]
        sift_down(heap, last)
        last -= 1


def main():
    with open(sys.argv[1]) as f:
        f.readline()
        a = map(int, f.readline().split())
        heap = []
        for i in a:
            add(heap, i)
        hs(heap)
        print(" ".join(map(str, heap)))

main()
