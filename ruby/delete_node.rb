# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end

# @param {ListNode} node
# @return {Void} Do not return anything, modify node in-place instead.
def delete_node(node)
    if node.nil?
        return
    end

    if node.next.nil?
        node = nil
        return
    end

    n = node.next
    node.val = n.val
    node.next = n.next
    n = nil
end

node0 = ListNode.new('0')
node1 = ListNode.new('0')
node2 = ListNode.new('0')
node0.next = node1
node1.next = node2
node2.next = nil

delete_node(node0)