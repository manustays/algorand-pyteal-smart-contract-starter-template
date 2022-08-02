# Setup

## Install dependencies:
1. Install [Git](https://github.com/git-guides/install-git)
2. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
3. Install [Algorand sandbox](https://github.com/algorand/sandbox)
4. 

3. Start Docker Desktop and goto the Sandbox folder

4. **Setup Sandbox:**
   1. Add this project folder as bind volume in sandbox `docker-compose.yml` under key `services.algod`:
      ```yml
      volumes:
        - type: bind
          source: <path to project folder>
          target: /data
      ```
    2. Start the Sandbox docker with the command: `./sandbox up -v`
    3. Other Sandbox commands (after starting it):
       1. Shut down the Sandbox: `./sandbox down`
       2. Get a list of test wallets/accounts: `./sandbox goal account list`
       3. Check the balance of an account (app account or wallet): `./sandbox goal balance --address <account-address>`
       4. Reset Sandbox (including the test accounts): `./sandbox reset`
5. **Setup your Project:**
   1.




4. Start sandbox:
    ```txt
    $ ./sandbox up
    ```
5. Install Python virtual environment in project folder:
    ```txt
    $ python -m venv venv
    $ source ./venv/Scripts/activate # Windows
    $ source ./venv/bin/activate # Linux
    ```
6. Use Python interpreter: `./venv/Scripts/python.exe`
    VSCode: `Python: Select Interpreter`


# Links

- [Official Algorand Smart Contract Guidelines](https://developer.algorand.org/docs/get-details/dapps/avm/teal/guidelines/)
- [PyTeal Documentation](https://pyteal.readthedocs.io/en/latest/index.html)
- [Algorand DevRel Example Contracts](https://github.com/algorand/smart-contracts)


# Credits
Forked from [algorand-devrel/pyteal-course](https://github.com/algorand-devrel/pyteal-course).