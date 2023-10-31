# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim

import heapq
import sys

def solution():
    # n for unread books in the heap
    # m for books that friend give
    # k for number of Jane Eyre has page
    n, m, k = map(int, input().split())
    book_unread =[sys.stdin.readline().strip() for _ in range(n)]
    book_unread = [(book.rsplit(' ', 1)[0].strip("\""), int(book.rsplit(' ', 1)[1])) for book in book_unread]
    book_friend = [sys.stdin.readline().strip() for _ in range(m)]
    book_friend = [(int(book.split(' ', 1)[0]), book.split(' ', 1)[1].rsplit(' ',1)[0].strip("\""), int(book.rsplit(' ', 1)[1])) for book in book_friend]
    #print(n, m, k)
    #print(book_unread)
    #print(book_friend)
    # Put JE and other unread books
    books = [("Jane Eyre", k)]
    for book in book_unread:
        books.append(book)
    # Heapify the books
    heapq.heapify(books)
    # Sort the friend given books
    book_friend.sort()
    time = 0
    idx = 0

    # For each book
    while books:
        title, pages = heapq.heappop(books)
        if title == "Jane Eyre":
            print(time+pages)
            return
        time += pages
        # Add friend given book according to given time
        while idx < m and book_friend[idx][0] <= time:
            time_received, title_received, pages_received = book_friend[idx]
            heapq.heappush(books, (title_received, pages_received))
            idx += 1


solution()