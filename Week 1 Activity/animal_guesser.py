#  Decison Tree - Animal Guesser    - Orion Group 34
#                    ┌────────────────────────┐
#                    │                        │
#                    │   HAS FEATHERS ?       │
#                    └──┬────────────────────┬┘
#                       │                    │
#                       │                    │
#              TRUE     │                    │ FALSE
#                       │                    │
#                       │                    │
#                       │                    │
#           ┌───────────▼──────┐         ┌───▼─────────────┐
#           │                  │         │                 │
#           │ CAN FLY ?        │         │ HAS FINS ?      ├──────────┐
#        ┌──┴───────────────┬──┘         └───────┬─────────┘          │
#        │                  │                    │                    │
#        │                  │                    │                    │
#  TRUE  │           FALSE  │            TRUE    │                    │  FALSE
#        │                  │                    │                    │
# ┌──────▼─────┐       ┌────▼────────┐   ┌───────▼───────┐    ┌───────▼───────┐
# │            │       │             │   │               │    │               │
# │ HAWK       │       │ PENGUIN     │   │ DOLPHIN       │    │ BEAR          │
# └────────────┘       └─────────────┘   └───────────────┘    └───────────────┘


print("Welcome to the Animal Guesser ! \n")
feather = input("Does the animal have feathers ? (Y/N): ")
if (feather == "Y" or feather == "y"):
  fly = input("can the animal fly ? (Y/N): ")
  if(fly == "Y" or fly == "y"):
    print("Hawk")
  else:
    print("Penguin")
elif (feather == "N" or feather == "n"):
  fin = input("does it have fins ? (Y/N): ")
  if(fin == "Y" or fin == "y"):
    print("Dolphin")
  else:
    print("Bear")
