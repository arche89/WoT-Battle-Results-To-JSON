_VEH_CELL_RESULTS_PUBLIC = ('health', 'credits', 'xp', 'achievementCredits', 'achievementXP', 'achievementFreeXP', 'shots', 'hits', 'thits', 'he_hits', 'pierced', 'damageDealt', 'damageAssistedRadio', 'damageAssistedTrack', 'damageReceived', 'shotsReceived', 'noDamageShotsReceived', 'heHitsReceived', 'piercedReceived', 'spotted', 'damaged', 'kills', 'tdamageDealt', 'tkills', 'isTeamKiller', 'capturePoints', 'droppedCapturePoints', 'mileage', 'lifeTime', 'killerID', 'achievements', 'potentialDamageReceived', 'isPrematureLeave')
_VEH_CELL_RESULTS_PRIVATE = ('repair', 'freeXP', 'details')
_VEH_CELL_RESULTS_SERVER = ('potentialDamageDealt', 'soloHitsAssisted', 'isEnemyBaseCaptured', 'stucks', 'autoAimedShots', 'presenceTime', 'spot_list', 'damage_list', 'kill_list', 'ammo', 'crewActivityFlags', 'series', 'tkillRating', 'tkillLog', 'destroyedObjects')
VEH_CELL_RESULTS = _VEH_CELL_RESULTS_PUBLIC + _VEH_CELL_RESULTS_PRIVATE + _VEH_CELL_RESULTS_SERVER
VEH_CELL_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_CELL_RESULTS)))
_VEH_BASE_RESULTS_PUBLIC = ('accountDBID', 'team', 'typeCompDescr', 'gold', 'deathReason')
_VEH_BASE_RESULTS_PRIVATE = ('xpPenalty', 'creditsPenalty', 'creditsContributionIn', 'creditsContributionOut')
_VEH_BASE_RESULTS_SERVER = ('eventIndices', 'vehLockTimeFactor', 'misc', 'cybersportRatingDeltas')
VEH_BASE_RESULTS = _VEH_CELL_RESULTS_PUBLIC + _VEH_BASE_RESULTS_PUBLIC + _VEH_CELL_RESULTS_PRIVATE + _VEH_BASE_RESULTS_PRIVATE + _VEH_CELL_RESULTS_SERVER + _VEH_BASE_RESULTS_SERVER
VEH_BASE_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_BASE_RESULTS)))
VEH_PUBLIC_RESULTS = _VEH_CELL_RESULTS_PUBLIC + _VEH_BASE_RESULTS_PUBLIC
VEH_PUBLIC_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_PUBLIC_RESULTS)))
VEH_FULL_RESULTS_UPDATE = ('tmenXP', 'isPremium', 'eventCredits', 'eventGold', 'eventXP', 'eventFreeXP', 'eventTMenXP', 'autoRepairCost', 'autoLoadCost', 'autoEquipCost', 'premiumXPFactor10', 'premiumCreditsFactor10', 'dailyXPFactor10', 'igrXPFactor10', 'aogasFactor10', 'markOfMastery', 'dossierPopUps', 'vehTypeLockTime', 'serviceProviderID')
VEH_FULL_RESULTS_UPDATE_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_FULL_RESULTS_UPDATE)))
_VEH_FULL_RESULTS_PRIVATE = ('originalCredits', 'originalXP', 'originalFreeXP', 'questsProgress')
VEH_FULL_RESULTS = _VEH_CELL_RESULTS_PUBLIC + _VEH_BASE_RESULTS_PUBLIC + _VEH_CELL_RESULTS_PRIVATE + _VEH_BASE_RESULTS_PRIVATE + VEH_FULL_RESULTS_UPDATE + _VEH_FULL_RESULTS_PRIVATE
VEH_FULL_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_FULL_RESULTS)))
PLAYER_INFO = ('name', 'clanDBID', 'clanAbbrev', 'prebattleID', 'team', 'igrType')
PLAYER_INFO_INDICES = dict(((x[1], x[0]) for x in enumerate(PLAYER_INFO)))
COMMON_RESULTS = ('arenaTypeID', 'arenaCreateTime', 'winnerTeam', 'finishReason', 'duration', 'bonusType', 'guiType', 'vehLockMode')
COMMON_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(COMMON_RESULTS)))
handled = 1
