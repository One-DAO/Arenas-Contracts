from brownie import (
    Contract,
    Metarenas,
    ArenasOld,
    ArenaToken,
    MetaPasses,
    ProxyAdmin,
    TransparentUpgradeableProxy,
    accounts,
)
from scripts.helpful_scripts import encode_function_data, getArenaRarities

verification = False


def main():
    # Deloy
    owner = accounts[0]
    # Deploy Proxi Admin
    proxy_admin = ProxyAdmin.deploy({"from": owner}, publish_source=verification)
    arena = ArenaToken.deploy({"from": owner}, publish_source=verification)
    passes = MetaPasses.deploy({"from": owner}, publish_source=verification)
    old_arenas = ArenasOld.deploy({"from": owner}, publish_source=verification)
    # Deploy the first MetaArenas implementation
    implementation = Metarenas.deploy({"from": owner}, publish_source=verification)
    # Encode the initializa function
    encoded_initializer_function = encode_function_data(implementation.initialize)
    print(encoded_initializer_function)
    proxy = TransparentUpgradeableProxy.deploy(
        implementation.address,
        proxy_admin.address,
        encoded_initializer_function,
        {"from": owner},
        publish_source=verification,
    )
    # Set Proxy ABI same as Implementation ABI
    meta_arenas = Contract.from_abi("Metarenas", proxy.address, Metarenas.abi)
    # Set the Address for interfaces in proxy
    meta_arenas.setInterfaces(
        old_arenas.address, passes.address, arena.address, {"from": owner}
    )
