
const tick = Date.now();
export const log = (v) => console.log(`${v} \n Elapsed: ${Date.now() - tick}ms`);

const codeBlocker = () => {
  // Blocking
  // let i = 0;
  // while(i < 1000000000) { i++;}
  // return '🐷 billion loops done';

  // While loop still runs on main thread :(
  // return new Promise((resolve, reject) => {

  //   let i = 0
  //   while(i < 1000000000) { i++;}
  //   resolve('🐷 billion loops done');
  // })

  // Putting code in resolved promise guarantees 
  // it will executed after all the synchronous 
  // code in the current macro task
  return Promise.resolve().then(v => {
    let i = 0
    while(i < 1000000000) { i++;}
    return '🐷 billion loops done';
  })
}

log('🥪 Synchronous 1');

// log(codeBlocker())
codeBlocker().then(log)

log('🥪 Synchronous 2');