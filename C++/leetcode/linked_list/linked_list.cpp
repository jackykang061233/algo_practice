#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev=nullptr;
        ListNode* current=head;
        while(current != nullptr){
            ListNode* next=current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        while(list1 != nullptr && list2 != nullptr){
            if (list1->val < list2->val){
                cur->next = list1;
                list1 = list1->next;
            }
            else{
                cur->next = list2;
                list2 = list2->next;
            }
            cur = cur->next;
        }
        if (list1 == nullptr){
            cur->next = list2;
        }
        else{
            cur->next = list1;
        }
        return dummy->next;
    }
};
int main()
{
    Solution solution;
    int x;
    cout << "Which question: ";
    cin >> x;

    // 206
    if (x==206){
        ListNode* node = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        ListNode* reversedList = solution.reverseList(node);
        while (reversedList != nullptr) {
            cout << reversedList->val << " ";
            reversedList = reversedList->next;
        }
    }

    // 21
    else if (x == 21){
        ListNode* list1 = new ListNode(1, new ListNode(2,  new ListNode(4)));
        ListNode* list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

        ListNode* mergedList = solution.mergeTwoLists(list1, list2);
        while (mergedList != nullptr) {
            cout << mergedList->val << " ";
            mergedList = mergedList->next;
        }
    }
    
    return 0;

}