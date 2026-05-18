class OrderFSM:
    def __init__(self):
        self.alphabet = ["E", "T", "K", "J", "C"]
        self.states = ["q0", "q1", "q2", "q3", "q4", "q5"]
        self.start_state = "q0"
        self.accept_states = {"q5"}
        self.state = self.start_state
        self.state_labels = {
            "q0": "Pilih event",
            "q1": "Pilih tanggal",
            "q2": "Pilih kategori",
            "q3": "Pilih jumlah",
            "q4": "Konfirmasi",
            "q5": "Selesai",
        }
        self.symbol_labels = {
            "E": "pilih event",
            "T": "pilih tanggal",
            "K": "pilih kategori",
            "J": "pilih jumlah",
            "C": "konfirmasi",
        }
        self.transitions = {
            ("q0", "E"): "q1",
            ("q1", "T"): "q2",
            ("q2", "K"): "q3",
            ("q3", "J"): "q4",
            ("q4", "C"): "q5",
        }
        self.trace = []

    def reset(self):
        self.state = self.start_state
        self.trace = []

    def step(self, symbol):
        key = (self.state, symbol)
        if key not in self.transitions:
            return False
        next_state = self.transitions[key]
        self.trace.append({"state": self.state, "symbol": symbol, "next_state": next_state})
        self.state = next_state
        return True

    def current_label(self):
        return self.state_labels[self.state]

    def transition_table(self):
        table = []
        for state in self.states:
            row = {"state": state}
            for symbol in self.alphabet:
                row[symbol] = self.transitions.get((state, symbol), "-")
            table.append(row)
        return table

    def language_definition(self):
        return {
            "alphabet": "{E, T, K, J, C}",
            "language": "L = { ETKJC }",
            "symbol_meanings": self.symbol_labels,
        }