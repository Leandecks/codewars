// TODO: create the User class/object
// it must support rank, progress and the incProgress(rank) method

class User {
  constructor() {
    this.rank = -8;
    this.progress = 0;
  }
  
  incProgress(n) {
    if (n > 8 || n < -8 || (n > -1 && n < 1)) {
      throw new Error();
    }
    if (n === this.rank) {
      this.prog(3);
    } else if (n === this.rank - 1) {
      this.prog(1);
    } else if (n > this.rank) {
      const d = n - this.rank;
      console.log(10 * d * d)
      this.prog(10 * d * d);
    }
  }

  prog(n) {
    let pro = this.progress + n;
    if (pro >= 100) {
      let rank_inc = Math.floor(pro / 100);
      let prog_inc = pro - rank_inc * 100;
      console.log(this.rank, this.rank + rank_inc);
      console.log("rankinc", rank_inc)
      if (this.rank <= -1 && this.rank + rank_inc > -1) {
        rank_inc += 2
      }
      this.rank += rank_inc;
      this.progress += prog_inc;
    } else {
      this.progress += n;
    }
  }
}

const u = new User();
u.incProgress(1);
console.log(u.rank);
console.log(u.progress);
