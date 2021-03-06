from p2p.peer import BasePeerContext
from trinity.db.beacon.chain import BaseAsyncBeaconChainDB


class BeaconContext(BasePeerContext):

    def __init__(self,
                 chain_db: BaseAsyncBeaconChainDB,
                 network_id: int,
                 client_version_string: str,
                 listen_port: int) -> None:
        super().__init__(client_version_string, listen_port)
        self.chain_db = chain_db
        self.network_id = network_id
