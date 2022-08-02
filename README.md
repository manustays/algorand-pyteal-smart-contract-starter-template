# Algorand PyTeal Starter Template
A basic starter template to learn PyTeal development for Algorand blockchain smart-contracts.


## Setup

### Install Dependencies
1. Install [Git](https://github.com/git-guides/install-git)
2. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
3. Install [Algorand sandbox](https://github.com/algorand/sandbox)
4. Copy this project without cloning:
   ```bash
   git clone -b main --depth 1 --single-branch git@github.com:manustays/algorand-pyteal-smart-contract-starter-template.git && rm -rf algorand-pyteal-smart-contract-starter-template/.git/
   ```


### Setup the Sandbox for Local Testing
1. Start Docker Desktop and goto the Sandbox folder
2. Add your project folder as bind volume in the Sandbox Docker image:
   - In the Sandbox root folder, edit the file `docker-compose.yml` and add the following lines under the key `services.algod`:
      ```yml
      volumes:
        - type: bind
          source: <path to this project folder>
          target: /data
      ```
3. Start the Sandbox docker container with the command: `./sandbox up -v`
4. **Other useful Sandbox commands** (after starting it):
    1. Shut down the Sandbox: `./sandbox down`
    2. Get a list of test wallets/accounts: `./sandbox goal account list`
    3. Check the balance of an account (app account or wallet): `./sandbox goal balance --address <account-address>`
    4. Reset Sandbox (including the test accounts): `./sandbox reset`


### Setup your Project
1. Goto project folder & setup Python virtual env for the project _(one time only)_: `python3 -m venv venv`
2. Activate the Python virtual environment _(everytime you start this project)_:
    ```bash
    $ ./venv/Scripts/activate # Windows
    $ ./venv/bin/activate # Linux/Mac
    ```
3. Check if virtual env is setup properly: `pip -V`
   - It should show the path to Python executable under your project's venv folder.
4. Install the python dependencies _(one time only)_: **`pip3 install -r requirements.txt`**


## Compile & Run
1. **Within the project folder:**
   1. Activate the Python virtual environment _(if not already done)_: `. venv/bin/activate`
   2. Build source files: `./build.sh contracts.<subfolder>.<filename-without-py-ext>`
2. **Within the Sandbox folder:**
   1. Enter the docker container terminal: `./sandbox enter algod`
   1. Check if project’s bound volume is working: `ls /data`
   1. Get test wallet accounts: `goal account list`
      ![Example](/img/1.png)
      - Copy account address in a variable for easy access: `WALLET1=F74DX......`
   1. Deploy contract within sandbox:
      ```bash
      goal app create --creator $WALLET1 --approval-prog /data/build/approval.teal --clear-prog /data/build/clear.teal --global-byteslices 1 --global-ints 3 --local-byteslices 0 --local-ints 0
      ```
      1. It returns a numeric app ID if successfully deployed (eg: 1)
      1. Store in a variable for easy access: `APPID=1`
   1. Get deployed app info: `goal app info --app-id $APPID`
       1. It returns application account, creator, approval hash, clear hash, etc.
       ![Example](/img/2.png)

   1. Read smart contract storage: `goal app read --global --app-id $APPID --guess-format`
       1. Returns a formatted JSON with all current global values
       ![Example](/img/3.png)

   1. Maintain minimum balance (0.1 algo or 100,000 microalgo) in the smart contract account:
       ```bash
       goal clerk send -f $WALLET1 -t $APP_ACCOUNT -a 100000
       ```
       1. [Algorand PyTeal Course | Transaction Fee Pooling and Minimum Balances - YouTube](https://www.youtube.com/watch?v=k3K9_UNlsFY&list=PLpAdAjL5F75CNnmGbz9Dm_k-z5I6Sv9_x&index=12)
   1. Call a Smart Contract Operation:
      ```bash
      goal app call --app-id $APPID --from $WALLET1 --app-arg "str:inc"
      ```
      1. Here, “inc” is the operation name as defined in the smart contract
      1. Check updated values *(counter incremented to one)*:
         ![Example](/img/4.png)

## Debug Smart Contract

Sandbox comes with the `tealdbg` tool for debugging. It requires a transaction dump file as input that we can generate while executing the smart-contract.

1. Generate the transaction dump file:
   ```bash
   goal app call --app-id $APPID --from $WALLET1 --app-arg "str:dec" **--dryrun-dump -o tx.dr**
   ```
1. Start debugger session:
   ```bash
   tealdbg debug -d tx.dr --listen 0.0.0.0
   ```
   ![Example](/img/6.png)
   1. The debug port (9392) can also be found from the `docker-compose.yml` file under the key: `CDT_PORT`.
1. Open the Chrome browser and goto `chrome://inspect/#devices`
   1. Click on “Configure” beside the “Discover network targets” option.
   1. Add `localhost:9392`
      ![Example](/img/7.png)
   1. Under “Remote Target”, look for the Algorand TEAL program and click on “inspect”.


## Links

- [Official Algorand Smart Contract Guidelines](https://developer.algorand.org/docs/get-details/dapps/avm/teal/guidelines/)
- [PyTeal Documentation](https://pyteal.readthedocs.io/en/latest/index.html)
- [Algorand DevRel Example Contracts](https://github.com/algorand/smart-contracts)
- [Awesome-Algorand](https://github.com/aorumbayev/awesome-algorand)


## Credits
- Forked from [algorand-devrel/pyteal-course](https://github.com/algorand-devrel/pyteal-course).
- Accompanying [tutorial on YouTube](https://www.youtube.com/playlist?list=PLpAdAjL5F75CNnmGbz9Dm_k-z5I6Sv9_x)
