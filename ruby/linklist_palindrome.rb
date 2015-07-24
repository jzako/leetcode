def print_linked_list(head)
    until head.nil?
        puts head.val
        head = head.next
    end
end

# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end

# @param {ListNode} head
# @return {Boolean}
def is_palindrome(head)
    if head.nil? or head.next.nil?
        return true
    end
    pre = head
    low = head.next
    fast = head.next.next
    head.next = nil
    until fast.nil?
        is_odd = true
        n = low.next
        low.next = pre
        pre = low
        low = n
        if fast.next.nil?
            fast = nil
            is_odd = true
        else
            fast = fast.next.next
            is_odd = false
        end
    end

    if is_odd
        pre = pre.next
    end

    flag = true
    until low.nil?
        if pre.val != low.val
            flag = false
            break
        end
        low = low.next
        pre = pre.next
    end

    return flag
end

input = ['a', 'a']

pre = nil
input.reverse!
input.each do |n|
    node = ListNode.new(n)
    node.next = pre
    pre = node
end

puts is_palindrome(pre)