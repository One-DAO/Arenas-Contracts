# Transparent Proxy ERC721 - Meta Arenas

# Test Scripts

## Tests the rewards accumulation for staking based on arena rarity

brownie test tests/test_rewards_accumulation.py -s

## Tests if the contract upgrades correctly

brownie test tests/test_upgrade_v2.py -s

## General test of the SC functionality

brownie test tests/test_upgradeable.py -s
