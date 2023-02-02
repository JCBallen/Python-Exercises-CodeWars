import os

os.system("cls")


class User:
    def __init__(self, rank=-8, progress=0):
        self.rank = rank
        self.progress = progress

    def inc_progress(self, q_rank):
        ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        # Excluding wrong ranks
        if q_rank not in ranks:
            print(f"Rank {q_rank} doesn't exist")
            raise
        # needed variables
        q_idx = ranks.index(q_rank)
        rank_idx = ranks.index(self.rank)
        diff = abs(q_idx-rank_idx)

        # point chart

        if q_idx + 1 == rank_idx:
            self.progress += 1
        if q_idx == rank_idx:
            self.progress += 3
        if q_idx > rank_idx:
            self.progress += 10*diff*diff

        # rank-up system detection
        if self.progress >= 100 or self.rank >= 8:
            aum_rank = self.progress//100
            self.rank = ranks[min(rank_idx+aum_rank, len(ranks)-1)]
            self.progress = self.progress % 100 if self.rank < 8 else 0


user = User()

print(user.rank)
print(user.progress)

user.inc_progress(6)  # ! ->3
# user.inc_progress(-1)
# user.inc_progress(1)
# user.inc_progress(-8)
user.inc_progress(7)
print(user.rank)
print(user.progress)
# user.inc_progress(8)
# user.inc_progress(3)
# user.inc_progress(5)

print(user.rank)
print(user.progress)
