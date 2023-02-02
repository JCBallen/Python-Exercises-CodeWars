import os

os.system("cls")


class User:
    def __init__(self, rank=-8, progress=0):
        self.rank = rank
        self.progress = progress

    def inc_progress(self, q_rank):
        # Excluding wrong ranks
        if q_rank == 0 or q_rank > 8 or q_rank < -8:
            print(f"Rank {q_rank} doesn't exist")
            raise
        # needed variables
        ignore_zero = False
        diff = abs(self.rank-q_rank)
        # to know if 0 ignoring is needed ex: -3 -> 1
        if q_rank > 0 and self.rank < 0:
            diff -= 1
            ignore_zero = True

        # point chart
        if q_rank == self.rank-1 or (q_rank == 1 and self.rank == -1):
            self.progress += 1
        if q_rank == self.rank:
            self.progress += 3
        if q_rank > self.rank:
            self.progress += 10*diff*diff

        # rank-up system detection
        if self.progress >= 100:
            old_rank = self.rank
            self.rank = self.rank + self.progress // 100 if self.rank + \
                self.progress // 100 <= 8 else 8
            self.rank = self.rank + \
                1 if self.rank == 0 or (
                    ignore_zero and self.rank > 0 and self.rank < 8) else self.rank
            self.progress = self.progress % 100 if self.rank < 8 else 0


user = User()
print(user.rank)

print(user.progress)

user.inc_progress(1)  # ! ->3
# user.inc_progress(-4)
# user.inc_progress(-7)
# user.inc_progress(6)
# user.inc_progress(3)
# user.inc_progress(8)
# user.inc_progress(3)
# user.inc_progress(5)

print(user.rank)

print(user.progress)
