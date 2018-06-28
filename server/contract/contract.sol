contract Voting {

    bytes32[] votingRecord;

    mapping (bytes32 => uint8) public votesReceived;

    string VotingTitle ;
    bytes32[] public candidateList;
    string originaltor;

    function Voting(string Title, string originaltor1, bytes32[] candidateNames) public {
        VotingTitle = Title;
        originaltor = originaltor1;
        candidateList = candidateNames;
    }

    function getVotesReceived() view public returns (bytes32[]) {
        return votingRecord;
    }

    function getOriginaltor() view public returns (string) {
        return originaltor;
    }

    function getTitle() view public returns (string) {
        return VotingTitle;
    }

    function getCandidateList() view public returns (bytes32[]) {
        return candidateList;
    }

    function totalVotesFor(bytes32 candidate) view public returns (uint8) {
        require(validCandidate(candidate));
        return votesReceived[candidate];
    }

    function voteForCandidate(bytes32 candidate, bytes32 record) public {
        require(validCandidate(candidate));
        votesReceived[candidate] += 1;
        votingRecord.push(record);
    }

    function validCandidate(bytes32 candidate) view public returns (bool) {
        for(uint i = 0; i < candidateList.length; i++) {
            if (candidateList[i] == candidate) {
                return true;
            }
        }
        return false;
    }
}